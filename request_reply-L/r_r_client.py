#help:              |  "Usage: CalculatorClient <x> <+|-|x|/> <y>"
#example            |  ./DDSCalculatorClient 3 x 6


import fastdds
import time

from build import operation


class Listener(fastdds.DataReaderListener):
    def __init__(self, calcul):
        self.calcul = calcul
        self._info = fastdds.SampleInfo()
        self._reply = operation.ReplyType()
        self.write_param = fastdds.WriteParams()
        self.z = None
        super().__init__()

    def on_data_available(self, reader):
        self.calcul.reply_reader_.take_next_sample(self._reply, self._info)

        if fastdds.ALIVE_INSTANCE_STATE == self._info.instance_state:
            print("---------")
            if True:  # self.write_param.sample_identity() == self._info.related_sample_identity():
                self.z = self._reply.z()



class ClientCalculate:
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
        self.request_writer_ = self.__publisher_.create_datawriter(self.__request_topic_, self.__writer_qos)
        self.__listener = Listener(self)
        self.__reader_qos.reliability().kind = fastdds.RELIABLE_RELIABILITY_QOS
        self.__reader_qos.durability().kind = fastdds.TRANSIENT_LOCAL_DURABILITY_QOS
        self.__reader_qos.history().kind = fastdds.KEEP_ALL_HISTORY_QOS
        self.reply_reader_ = self.__subscriber_.create_datareader(self.__reply_topic_, self.__reader_qos, self.__listener)

    def request(self):
        request = operation.RequestType()
        request.operation(operation.ADDITION)
        request.x(3)
        request.y(4)

        self.request_writer_.write(request, self.__listener.write_param)

        time.sleep(3)
        return self.__listener.z



client = ClientCalculate()
z = client.request();
print(z)

