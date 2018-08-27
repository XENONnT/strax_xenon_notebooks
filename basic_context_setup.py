import strax 

# Set S3_ACCESS_KEY and S3_SECRET_ACCESS_KEY environmental variables

cache_data_directory = '.'  # Maybe change this where you want new files to go

st = strax.Context(register_all=strax.xenon.plugins,
                   storage=[strax.DataDirectory(cache_data_directory),
                            strax.SimpleS3Store(readonly=True)],
                   config={'pax_raw_dir' : './'})

# This is needed since data came from XENON1T (you don't need pax)
st.register(strax.xenon.pax_interface.RecordsFromPax)
dataset = '170319_0510'
print(st.get_df(dataset, 'event_info').head())
