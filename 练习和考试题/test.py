import requests

url = "https://192.168.53.151:8081/services/ArServices"

payload = "<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:ars=\"http://www.huawei.com/bme/cbsinterface/arservices\" xmlns:cbs=\"http://www.huawei.com/bme/cbsinterface/cbscommon\" xmlns:arc=\"http://cbs.huawei.com/ar/wsservice/arcommon\">\n   <soapenv:Header/>\n   <soapenv:Body>\n      <ars:RechargeRequestMsg>\n         <RequestHeader>\n            <cbs:Version>1</cbs:Version>\n            <!--Optional:-->\n            <cbs:BusinessCode>Recharge</cbs:BusinessCode>\n            <cbs:MessageSeq></cbs:MessageSeq>\n            <!--Optional:-->\n            <cbs:OwnershipInfo>\n               <cbs:BEID>101</cbs:BEID>\n            </cbs:OwnershipInfo>\n            <cbs:AccessSecurity>\n               <cbs:LoginSystemCode>102</cbs:LoginSystemCode>\n               <cbs:Password>v7fqKAe5C0XY5bvuX6G+FiRQZSj0YOoSGhxMIPiD7f0ZVV9DrLLphnVsp012uw==</cbs:Password>\n            </cbs:AccessSecurity>\n            <cbs:OperatorInfo>\n               <cbs:OperatorID>Bred</cbs:OperatorID>\n            </cbs:OperatorInfo>\n         </RequestHeader>\n         <RechargeRequest>\n            <!--Optional:-->\n            <ars:RechargeSerialNo></ars:RechargeSerialNo>\n            <ars:RechargeObj>\n               <!--You have a CHOICE of the next 2 items at this level-->\n               <ars:SubAccessCode>\n                  <!--You have a CHOICE of the next 2 items at this level-->\n                  <arc:PrimaryIdentity>73511995</arc:PrimaryIdentity>\n               </ars:SubAccessCode>\n            </ars:RechargeObj>\n            <ars:RechargeInfo>\n               <!--You have a CHOICE of the next 2 items at this level-->\n               <!--1 or more repetitions:-->\n               <ars:CashPayment>\n                  <!--Optional: cash-->\n                  <ars:PaymentMethod>1001</ars:PaymentMethod>\n                  <ars:Amount>2500</ars:Amount>\n               </ars:CashPayment>\n            </ars:RechargeInfo>\n            <!--Optional SBD:-->\n            <ars:CurrencyID>1126</ars:CurrencyID>\n         </RechargeRequest>\n      </ars:RechargeRequestMsg>\n   </soapenv:Body>\n</soapenv:Envelope>"

headers = {
    'Content-Type': 'text/xml; charset=utf-8',
    'SOAPAction': 'Recharge'
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)

print(response.text)
