from facebook_business.adobjects.user import User
from facebook_business.api import FacebookAdsApi

app_id = 'COLOCAR_AQUI_SEU_ID_DE_APP'
app_secret = 'COLOCAR_AQUI_SUA_CHAVE_SECRETA'
access_token = 'COLOCAR_AQUI_SEU_TOKEN_DE_ACESSO'

FacebookAdsApi.init(app_id, app_secret, access_token)

me = User(fbid='me')
my_accounts = list(me.get_ad_accounts())
print(my_accounts)
