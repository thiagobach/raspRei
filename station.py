from websocket_server import WebsocketServer
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(' %(module)s -  %(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# a[0]:pos , a[1]:goal if pos == goal then switch
def switch(client, server, a):
    logger.info('pos:{},goal:{}'.format(a[0],a[1]))
    if a[0] == a[1]:
        # add method to switch
        server.send_message_to_all("SWITCH")
    return True


if __name__ == "__main__":
    server = WebsocketServer(13254, host='127.0.0.1', loglevel=logging.INFO)
    server.set_fn_message_received(switch)
    server.run_forever()
