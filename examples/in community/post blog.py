import amino

client = amino.Client()
client.login(email='YOUR EMAIL', password='YOUR PASSWORD')
subclient = amino.SubClient(comId='COMMUNITY ID', profile=client.profile)

subclient.post_blog('TITLE', 'CONTENT')