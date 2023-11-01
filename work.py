import streamlit as st
st.set_page_config(page_title ='my game',page_icon='random')
mymenu=st.sidebar.selectbox('My Menu',('Home','Fillfrom','Downloads'))
st.image('https://ecn.dev.virtualearth.net/REST/v1/Imagery/Map/RoadVibrant/Routes/driving?ms=266,166&culture=en-in&waypoint.1=28.6812610626221,77.0739135742188;drsp.f;+&waypoint.2=28.6690807342529,77.4304122924805;drep.f;+&mapLayer=TrafficFlow,Basemap,trafficroute,OsmBuildings&key=AugYTsAbLKj7moSUfsxalWlCFq3qnO8wjRy5Pp4tXwCpwW0gClh_Eq0gwMSHPcLK&fmt=png&da=ro&logo=n')
st.title('Host only')
st.header('shivam jha')
st.text('this is the stream of science')
if (mymenu=='Home'):
	st.image('https://th.bing.com/th?id=ORMS.ff1957aaa1d22c5745c2658de2b099b9&pid=Wdp&w=300&h=156&qlt=90&c=1&rs=1&dpr=1.25&p=0')
	st.markdown('<center><h1>WELCOME</h1></center>',unsafe_allow_html=True)
	st.video('https://www.youtube.com/watch?v=8jRLGR8KrbE')
elif(mymenu=='Fillfrom'):
	with st.form('My From'):
		name=st.text_input('Enter the Name')
		dob=st.date_input("choose Date of Birth")
		marks=st.slider('choose Marks')
		k=st.form_submit_button("Sumit Form")
		if k:
			st.write('Name',name,'DOB',dob,'Marks',marks)
elif(mymenu=='Downloads'):
	st.header("Downloads")
	st.download_button('Doenload Now','hello this is the downloade data','onlei.txt')