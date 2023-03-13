import fastdds
import time

from build import operation


class Listener(fastdds.DataReaderListener):
    def __init__(self, calcul):
        self.calcul = calcul
        self._info = fastdds.SampleInfo()
        self._request = operation.RequestType()
        super().__init__()

    def on_data_available(self, reader):
        self.calcul.request_reader_.take_next_sample(self._request, self._info)

        if fastdds.ALIVE_INSTANCE_STATE == self._info.instance_state:
            print("++++++++")
            replay_data = operation.ReplyType()

            if operation.ADDITION == self._request.operation():
                replay_data.z(self._request.x() + self._request.y())

            elif operation.SUBSTRACTION == self._request.operation():
                replay_data.z(self._request.x() - self._request.y())

            elif operation.MULTIPLICATION == self._request.operation():
                replay_data.z(self._request.x() * self._request.y())

            elif operation.DIVISION == self._request.operation():
                if not self._request.y() == 0:
                    replay_data.z(self._request.x() / self._request.y())

            write_params = fastdds.WriteParams()
            write_params.related_sample_identity().writer_guid(self._info.sample_identity.writer_guid())
            write_params.related_sample_identity().sequence_number(
                self._info.sample_identity.sequence_number())
            self.calcul.reply_writer_.write(replay_data, write_params)
            print(replay_data)

class ServerCalculate:
    def __init__(self):
        self.__reply_type = operation.ReplyTypePubSubType()
        self.__request_type = operation.RequestTypePubSubType()
        self.__factory = fastdds.DomainParticipantFactory.get_instance()  # mine add
        self.__participant_qos = fastdds.DomainParticipantQos()  # mine add
        self.__factory.get_default_participant_qos(self.__participant_qos)  # my add
        self.__participant_ = self.__factory.create_participant(0,self.__participant_qos)

        self.__type_support_reply = fastdds.TypeSupport(self.__reply_type)  # mine add
        self.__type_support_request = fastdds.TypeSupport(self.__request_type)  # mine add
        self.__participant_.register_type(self.__type_support_reply)
        self.__participant_.register_type(self.__type_support_request)

        self.__publisher_ = self.__participant_.create_publisher(fastdds.PUBLISHER_QOS_DEFAULT)
        self.__subscriber_ = self.__participant_.create_subscriber(fastdds.SUBSCRIBER_QOS_DEFAULT)

        self.__reply_type.setName("ReplyType")
        self.__request_type.setName("RequestType")
        self.__request_topic_ = self.__participant_.create_topic("CalculatorRequest", self.__request_type.getName(), fastdds.TOPIC_QOS_DEFAULT)
        self.__reply_topic_ = self.__participant_.create_topic("CalculatorReply", self.__reply_type.getName(), fastdds.TOPIC_QOS_DEFAULT)

        self.__writer_qos = fastdds.DataWriterQos()
        self.__reader_qos = fastdds.DataReaderQos()
        self.__subscriber_.get_default_datareader_qos(self.__reader_qos)
        self.__writer_qos.history = fastdds.KEEP_ALL_HISTORY_QOS
        self.reply_writer_ = self.__publisher_.create_datawriter(self.__reply_topic_, self.__writer_qos)
        self.__listener = Listener(self)
        self.__reader_qos.reliability().kind = fastdds.RELIABLE_RELIABILITY_QOS
        self.__reader_qos.durability().kind = fastdds.TRANSIENT_LOCAL_DURABILITY_QOS
        self.__reader_qos.history().kind = fastdds.KEEP_ALL_HISTORY_QOS
        self.request_reader_ = self.__subscriber_.create_datareader(self.__request_topic_, self.__reader_qos, self.__listener)


server = ServerCalculate()
while 1:
    time.sleep(1)