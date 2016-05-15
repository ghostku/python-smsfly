import os

import requests as req
from requests.auth import HTTPBasicAuth


class SMSFlyAPI:

    def __init__(self, account_id=os.getenv('SMSFLY_ID'), account_pass=os.getenv('SMSFLY_PASS')):
        session = req.Session()
        session.auth = HTTPBasicAuth(account_id, account_pass)
        self.__http = session

    def send_sms_to_recipient(self, *, start_time, end_time, lifetime, rate, desc, source, body, recipient):
        return self.__sendsms(start_time, end_time, lifetime, rate, desc, source,
                              message_pairs=(body, recipient), individual_mode=False)

    def send_sms_to_recipients(self, *, start_time, end_time, lifetime, rate, desc, source, body, recipients):
        message_pairs=list(map(lambda r: [r], recipients))
        message_pairs[0][1] = body
        return self.__sendsms(start_time, end_time, lifetime, rate, desc,
                              source, message_pairs, individual_mode=False)

    def send_sms_pairs(self, *, start_time, end_time, lifetime, rate, desc, source, message_pairs):
        return self.__sendsms(start_time, end_time, lifetime, rate, desc,
                              source, message_pairs, individual_mode=True)

    def __sendsms(self, start_time, end_time, lifetime, rate, desc,
                  source, message_pairs, individual_mode=False):
        add_body = True
        for recipient, body in message_pairs:
            if not individual_mode:
                if add_body:
                    add_body = not add_body
                    # add body of message_pairs[0][1]
            else:
                # add body
                pass
            # add recipient
        return

    def __getcampaigninfo(self, *, campaign_id):
        pass

    def __getcampaigndetail(self, *, campaign_id):
        pass

    def __getmessagestatus(self, *, campaign_id, recipient):
        pass

    def __getbalance(self):
        pass

    def add_alphaname(self, alphaname):
        return self.__managealfaname(command_id='ADDALFANAME', alfaname=alphaname)

    def check_alphaname(self, alphaname):
        return self.__managealfaname(command_id='CHECKALFANAME', alfaname=alphaname)

    def get_alphanames_list(self):
        return self.__managealfaname(command_id='GETALFANAMESLIST')

    def __managealfaname(self, *, command_id, alfaname=None):
        pass
