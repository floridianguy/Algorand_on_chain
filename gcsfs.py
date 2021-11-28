
fs = gcsfs.GCSFileSystem(token='json1.json' ,project='your project name in GCP')# upload
with fs.open('ETL_load1.csv') as youralias:df = pd.read_csv(alias)fs.upload("Documents/tmp/ETL_load1.csv",'bucket/ETL_load1.csv')
