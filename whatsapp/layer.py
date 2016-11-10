from yowsup.layers.interface import YowInterfaceLayer, ProtocolEntityCallback

from models import WhatsappReceived

import datetime

class EchoLayer(YowInterfaceLayer):

    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):

        if messageProtocolEntity.getType() == 'text':
            self.onTextMessage(messageProtocolEntity)
        elif messageProtocolEntity.getType() == 'media':
            self.onMediaMessage(messageProtocolEntity)
        else:
            print('es otro tipo de media')
            print(messageProtocolEntity.getType())

        self.toLower(messageProtocolEntity.forward(messageProtocolEntity.getFrom()))
        self.toLower(messageProtocolEntity.ack())
        self.toLower(messageProtocolEntity.ack(True))


    @ProtocolEntityCallback("receipt")
    def onReceipt(self, entity):
        try:
            self.toLower(entity.ack())
        except Exception as e:
            print(e)

    def onTextMessage(self,messageProtocolEntity):
        # just print info
        print("Echoing %s to %s" % (messageProtocolEntity.getBody(), messageProtocolEntity.getFrom(False)))
        message = messageProtocolEntity.getBody()
        phone = messageProtocolEntity.getFrom(False)
        dbphone = WhatsappReceived.objects.filter(phone=phone).order_by('-date_creation')
        len_dbphone = len(dbphone)
        if len_dbphone > 0:
            now = datetime.datetime.now()
            if dbphone[0].date_creation.date() == now.date() and\
                    now < (dbphone[0].date_creation\
                    + datetime.timedelta(minutes=2)):
                last_message = dbphone[0].message
                try:
                    current_message = last_message + '\n' + message
                    dbphone[0].update(message=current_message)
                except Exception as e:
                    pass
            else:
                whatsapp = WhatsappReceived(phone=phone,
                                            message=message,
                                            image=None,
                                            is_valid=False,
                                            is_complete=False,
                                            date_creation=datetime.datetime.now())
                whatsapp.save()

        else:
            whatsapp = WhatsappReceived(phone=phone,
                                        message=message,
                                        image=None,
                                        is_valid=True,
                                        is_complete=False,
                                        date_creation=datetime.datetime.now())
            whatsapp.save()
        messageProtocolEntity.setBody('Gracias por su mensaje')

    def onMediaMessage(self, messageProtocolEntity):
        # just print info
        if messageProtocolEntity.getMediaType() == "image":
            print("Echoing image %s to %s" % (messageProtocolEntity.url, messageProtocolEntity.getFrom(False)))

        elif messageProtocolEntity.getMediaType() == "audio":
            print("Echoing audio %s to %s" % (messageProtocolEntity.url, messageProtocolEntity.getFrom(False)))

        elif messageProtocolEntity.getMediaType() == "video":
            print("Echoing video %s to %s" % (messageProtocolEntity.url, messageProtocolEntity.getFrom(False)))

        elif messageProtocolEntity.getMediaType() == "location":
            print("Echoing location (%s, %s) to %s" % (messageProtocolEntity.getLatitude(), messageProtocolEntity.getLongitude(), messageProtocolEntity.getFrom(False)))

        elif messageProtocolEntity.getMediaType() == "vcard":
            print("Echoing vcard (%s, %s) to %s" % (messageProtocolEntity.getName(), messageProtocolEntity.getCardData(), messageProtocolEntity.getFrom(False)))
        else:
            print(messageProtocolEntity.getMediaType())

