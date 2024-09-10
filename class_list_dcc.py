import xml.dom.minidom
class Class_Listas_DCC:
	
	def __init__(self):
		self.STATIC_ITEMS = ['plan', 'zlevel', 'lc', 'sw', 'tk', 'tx', 'bk', 'sg', 'fb', 'co' ]
		# self.ITEM = ""

	# Lista de los items según su tipo (plan, zlevel..)
	# @ data: Documento xml.dom.minidom.Document
	# @ item_type: String con el tipo de item plan, zlevel...
	# @ return: Devuelve una lista con los items
	def Single_items_list(self, data, item_type):
		datas = []
		item_ = ""
		# print(f"Single Items List self.ITEM: {self.ITEM}, desde {item_type}")
		if item_type == 'ini':
			self.get_nice_rocrail_ini(item_type)
		else:
			items = data.getElementsByTagName(item_type)
			for item in items:
				# plan y zlevel no se almacena como "id", si no como "title"
				if item_type == self.STATIC_ITEMS[0] or item_type == self.STATIC_ITEMS[1]: # plan y zlevel
					item_ = item.getAttribute('title')
				else: 	
					item_ = item.getAttribute('id')
				itm_ = "Id: " + item_
				datas.append(itm_)
		return datas
		
	# Lista de los items 'tk' según su atributo 'id'
	# @ data: Documento xml.dom.minidom.Document
	# @ tag: String con el atributo id del item
	# @ return: Devuelve una lista con items 'tk'
	def get_tracks(self, data, tag):
		items = data.getElementsByTagName(self.STATIC_ITEMS[4])
		for item in items:
			if tag == item.getAttribute('id'):
				track_ =[{ 'id': item.getAttribute('id')
						, 'type': item.getAttribute('type'), 'ori': item.getAttribute('ori')
			            , 'x': item.getAttribute('x'), 'y': item.getAttribute('y')
	 	                , 'z': item.getAttribute('z'), 'prev_id': item.getAttribute('prev_id')
		                , 'blockid': item.getAttribute('blockid'), 'senid: ': item.getAttribute('sensorid')
		   	            , 'road': item.getAttribute('road'), 'routeids': item.getAttribute('routeids')
		  	            , 'tknr': item.getAttribute('tknr')
		   		        }]
				return track_

	# Lista de los items 'fb' según su atributo 'id'
	# @ data: Documento xml.dom.minidom.Document
	# @ tag: String con el atributo id del item 
	# @ return: Devuelve una lista con items 'fb'
	def get_sensors(self, data, tag):
		items = data.getElementsByTagName(self.STATIC_ITEMS[8])
		try:
			for item in items:
				if tag == item.getAttribute('id'):
					sensor_ =[{ 'id': item.getAttribute('id')
							, 'type': item.getAttribute('type'), 'ori': item.getAttribute('ori')
				            , 'x': item.getAttribute('x'), 'y': item.getAttribute('y')
	 		                , 'z': item.getAttribute('z'), 'prev_id': item.getAttribute('prev_id')
			                , 'blockid': item.getAttribute('blockid'), 'senid: ': item.getAttribute('sensorid')
			   	            , 'road': item.getAttribute('road'), 'routeids': item.getAttribute('routeids')
			  	            , 'curve': item.getAttribute('curve'), 'tknr': item.getAttribute('tknr')
			  	            , 'operable' : item.getAttribute("operable"), 'addr' : item.getAttribute("addr")
			  	            , 'timer' : item.getAttribute("timer"), 'counter' : item.getAttribute("counter")
			  	            , 'state' : item.getAttribute("state")
	
			   		            }]
					return sensor_
		except Exception as err:
			print("Error:", err)
			pass

	# Lista de los items 'sg' según su atributo 'id'
	# @ data: Documento xml.dom.minidom.Document
	# @ tag: String con el atributo id del item
	# @ return: Devuelve una lista con items 'sg'	
	def get_signals(self, data, tag):
		# print(f"datos: {data}, tag: {tag}")
		items = data.getElementsByTagName(self.STATIC_ITEMS[7])
		for item in items:
			if tag == item.getAttribute('id'):
				signal_ =[{ 'id': item.getAttribute('id')
						, 'type': item.getAttribute('type'), 'ori': item.getAttribute('ori')
			            , 'x': item.getAttribute('x'), 'y': item.getAttribute('y')
	 	                , 'z': item.getAttribute('z'), 'prev_id': item.getAttribute('prev_id')
		                , 'blockid': item.getAttribute('blockid'), 'senid: ': item.getAttribute('sensorid')
		   	            , 'road': item.getAttribute('road'), 'routeids': item.getAttribute('routeids')
		  	            , 'curve': item.getAttribute('curve') , 'tknr': item.getAttribute('tknr')
		  	            , 'operable' : item.getAttribute("operable"), 'state' : item.getAttribute("state")
		  	            , 'addr1' : item.getAttribute("addr1"), 'port1' : item.getAttribute("port1")
		  	            , 'manual' : item.getAttribute("manual")
		   		            }]
				return signal_

	# Lista de los items 'lc' según su atributo 'id'
	# @ data: Documento xml.dom.minidom.Document
	# @ tag: String con el atributo id del item
	# @ return: Devuelve una lista con items 'lc'	
	def get_locomotive(self, data, tag):
		# print(f"datos: {data}, tag: {tag}")
		items = data.getElementsByTagName(self.STATIC_ITEMS[2]) # 'lc'
		for item in items:
			if tag == item.getAttribute('id'):
				loc_ =[{ 'id': item.getAttribute('id')
						, 'addr': item.getAttribute('addr'), 'iid': item.getAttribute('iid')
			            , 'image': item.getAttribute('image'), 'spcnt': item.getAttribute('spcnt')
	 	                , 'V_min': item.getAttribute('V_min'), 'V_mid': item.getAttribute('V_mid')
		                , 'V_cru': item.getAttribute('V_cru'), 'V_max: ': item.getAttribute('V_max')
		   	            , 'active': item.getAttribute('active'), 'number': item.getAttribute('number')
		  	            , 'engine': item.getAttribute('engine') , 'era': item.getAttribute('era')
		  	            , 'nraxis': item.getAttribute('nraxis') , 'color': item.getAttribute('color')
		  	            , 'show': item.getAttribute('show')
		   		            }]
				return loc_

	# Lista de los items 'sw' según su atributo 'id'
	# @ data: Documento xml.dom.minidom.Document
	# @ tag: String con el atributo id del item
	# @ return: Devuelve una lista con items 'sw'	
	def get_switchs(self, data, tag):
		# print(f"datos: {data}, tag: {tag}")
		items = data.getElementsByTagName(self.STATIC_ITEMS[3]) # 'sw'
		for item in items:
			if tag == item.getAttribute('id'):
				sw_ =[{ 'id': item.getAttribute('id')
						, 'swtype': item.getAttribute('swtype'), 'ori': item.getAttribute('ori')
			            , 'x': item.getAttribute('x'), 'y': item.getAttribute('y')
	 	                , 'z': item.getAttribute('z'), 'type': item.getAttribute('type')
	 	                , 'addr1': item.getAttribute('addr1'), 'port1': item.getAttribute('port1')
		                , 'state': item.getAttribute('state'), 'outoforder: ': item.getAttribute('outoforder')
		   	            , 'operable': item.getAttribute('operable'), 'frogaccessory': item.getAttribute('frogaccessory')
		  	            , 'frogswitch': item.getAttribute('frogswitch') , 'froginvert': item.getAttribute('froginvert')
		  	            , 'switched': item.getAttribute('switched')
		   		            }]
				return sw_

	
	# Tag: 'plan'
	def get_plan_nice_list(self, data, tag):
		items = data.getElementsByTagName(self.STATIC_ITEMS[0])
		for item in items:
			if tag == item.getAttribute('title'):
				roc_ = ( 'Plan name: ' + item.getAttribute('title') 
            	        	+ '\nPath: ' + item.getAttribute('rocrailpwd') + '\nHealthy? ' + item.getAttribute('healthy')
            	            + '\nScale: 1/' + item.getAttribute('scale') + '\nVersion: ' + item.getAttribute('rocrailversion') 
            	            + '\nArchitecture: ' + item.getAttribute('rocrailarch') + '\nOS: ' + item.getAttribute('rocrailos')
            	            + '\nRocrail IP: ' + item.getAttribute('rocrailip')
            	        )
				return roc_

				'''
				<plan 
				* rocrailversion="2.1.3131" 
				* rocrailpwd="/home/peyu/snap/Rocrail/Maqueta_modular" 
				* rocrailos="linux" 
				* rocrailarch="X86_64" 
				* rocrailip="192.168.1.37" 
				donkey="false" 
				* healthy="true" 
				* title="MaquetaModularMadera" 
				remark="" 
				* scale="87" 
				metrics="0"
				>
				'''

	# Tag 'zleve'
	def get_level_nice_list(self, data, tag):
		items = data.getElementsByTagName(self.STATIC_ITEMS[1])
		for item in items:
			if tag == item.getAttribute('title'):
				level_ = ( 'Level name: ' + item.getAttribute('title') 
				            + '\nTab id: ' + item.getAttribute('tabidx') 
				            + '\nSymbol prefix: '+ item.getAttribute('symbolprefix')
				            )
				return level_

	# Tag 'lc'
	def get_locomotives_nice_list(self, data, tag):
		items = data.getElementsByTagName(self.STATIC_ITEMS[2])
		for item in items:
			if tag == item.getAttribute('id'):
				cab_ = ( "Loc: " + item.getAttribute('id') 
            	                + '\nDCC:' + item.getAttribute('addr') + '\nSteeps:'+ item.getAttribute('spcnt') 
            	                + '\nInterface: '+ item.getAttribute("iid") + '\nNumber: ' + item.getAttribute('number')
            	                + '\nColor: ' + item.getAttribute('color') + '\nShow? ' + item.getAttribute('show')
            	                + '\nActive? ' + item.getAttribute('active') + '\nUse schedule time? ' + item.getAttribute('usescheduletime')
            	                + '\nSpeeds: Vmin:'+ item.getAttribute('V_min') + '\tVmid:'+ item.getAttribute('V_mid') 
            	                + '\tVcru:'+ item.getAttribute('V_cru')  + '\tVmax:'+ item.getAttribute('V_max')
            	                + '\nEngine:'+ item.getAttribute('engine') + "\nN. ejes: " + item.getAttribute("nraxis") 
            	                + "\nEpoca: " + item.getAttribute("era")
            	                + '\nImagen:'+ item.getAttribute('image')
            	                + '\nDescription:'+ item.getAttribute("desc"))
				return cab_
				'''
				<lc 
				* id="NS2418" 
				* image="ns2418.png" 
				prev_id="NS2418" 
				shortid="" 
				roadname="Nederlands 
				Spoorwegen" 
				owner="" 
				color="" 
				number="2418" 
				home="" 
				desc="" 
				dectype="" 
				decfile="nmra-rp922.xml" 
				docu="" 
				imagenr="0" 
				remark="" 
				len="0" 
				weight="0" 
				nrcars="0" 
				manuid="" 
				catnr="" 
				purchased="" 
				value="" 
				identifier="2418" 
				show="true" 
				useshortid="false" 
				mint="0" 
				throttlenr="0" 
				manually="false" 
				bus="0" 
				addr="2418" 
				secaddr="0" 
				iid="" 
				oid="" 
				prot="P" 
				protver="1" 
				spcnt="128" 
				secspcnt="14" 
				fncnt="4" 
				* V_min="10" 
				* V_mid="50" 
				* V_cru="80" 
				* V_max="100" 
				V_maxsec="14" 
				KMH_min="0" 
				KMH_mid="0" 
				KMH_cru="0" 
				KMH_max="0" 
				KMH_Rmin="0" 
				KMH_Rmid="0" 
				KMH_Rcru="0" 
				KMH_Rmax="0" 
				V_Rmin="0" 
				V_Rmid="0" 
				V_Rcru="0" 
				V_Rmax="0" 
				V_step="0" 
				mass="0" 
				Vmidpercent="30"
				Vmaxmin="20" 
				Vmaxmax="255" 
				Vmaxkmh="0" 
				Vmidset="true" 
				V_mode="percent" 
				placing="true" 
				regulated="true" 
				restorefx="false" 
				restorefxalways="false" 
				restorespeed="false" 
				info4throttle="false" 
				dirpause="0" 
				adjustaccel="false" 
				maxload="0" 
				accelmin="0" 
				accelmax="0" 
				decelerate="0" 
				blockwaittime="10" 
				maxwaittime="0" 
				evttimer="0" 
				minenergypercentage="0" 
				swaptimer="0" 
				ent2incorr="100" 
				priority="10" 
				usescheduletime="false" 
				commuter="true" 
				shortin="false" 
				inatpre2in="false" 
				usemanualroutes="false" 
				useownwaittime="false" 
				startupscid="" 
				startuptourid="" 
				check2in="false" 
				usedepartdelay="true" 
				freeblockonenter="false" 
				reducespeedatenter="false" 
				routespeedatenter="false" 
				v0onswap="false" 
				resetplacing="false" 
				manual="false" 
				lookupschedule="false" 
				lookupschedulevirtual="false" 
				generated="false" 
				engine="diesel" 
				cargo="none" 
				secondnextblock="false" 
				secondnextblock4wait="false" 
				era="0" 
				class="" 
				consist_syncfunmap="0" 
				consist_lightsoff="false" 
				consist_syncfun="false" 
				consist_synclights="false" 
				consist="" 
				usebbt="false" 
				bbtsteps="10" 
				bbtstartinterval="10" 
				bbtmaxdiff="250" 
				bbtcorrection="25" 
				bbtkey="0" 
				cvnrs="1,2,3,4,5,6,17,18,29" 
				destblockid="" 
				cmdDelay="0" 
				mode="stop" 
				fifotop="false" 
				energypercentage="0" 
				V="0" 
				fx="0" 
				throttleid="" 
				trainlen="0" 
				trainweight="0" 
				blockid="cb4" 
				blockenterid="" 
				resumeauto="false" 
				modereason="" 
				waittime="0" 
				V_hint="mid" 
				blockenterside="true" 
				dir="true" 
				fn="true" 
				mtime="0" 
				rdate="0" 
				active="true" 
				scidx="-1" 
				scheduleid="" 
				tourid="" 
				train="" 
				V_realkmh="0" 
				V_maxkmh="0" 
				cmd="modify" 
				signalaspect="" 
				pause="false" 
				screcord="false"/>
				'''

	# Tag 'sw'
	def get_turnout_nice_list(self, data, tag):
		items = data.getElementsByTagName(self.STATIC_ITEMS[3])        
            
		for item in items:
			if tag == item.getAttribute('id'):
				
				turnout_ = ( 'Turnout name: ' + item.getAttribute('id') + '\nDescription: ' + item.getAttribute('desc')
				            + '\nUse short ID? ' + item.getAttribute('useshortid') + '\nShort ID: ' + item.getAttribute('shortid')
							+ '\nSwitched ' + item.getAttribute('switched') + ' times'
				            + '\nType: ' + item.getAttribute('type') + '\nSaved position: ' + item.getAttribute('savepos')
				            + '\nSwitch type: ' + item.getAttribute('swtype')
				            + '\nState? ' + item.getAttribute('state') + '\nOut of order?: ' + item.getAttribute('outoforder')
				            + '\nShow? ' + item.getAttribute('show') + '\ndelay: ' + item.getAttribute('delay') + ' ms'
				            + '\nOrientation: '+ item.getAttribute('ori') + '\nInterface: ' + item.getAttribute('iid') 
				            + '\nOperable? ' + item.getAttribute('operable') 
				            + '\nAddress: ' + item.getAttribute('addr1') + '\nPort: ' + item.getAttribute('port1')
				            + '\nFrog accesory? ' + item.getAttribute('frogaccessory') + '\nFrog switch? ' + item.getAttribute('frogswitch') 
				            + '\nFrog invert? ' + item.getAttribute('froginvert')
				            + '\nX axis: ' + item.getAttribute('x') + '\nY axis: ' + item.getAttribute('y')
				            + '\nZ axis: ' + item.getAttribute('z') 
				            )
				return turnout_

				'''
				<sw 
				type="accessory" 
				accnr="10" 
				id="rc1" 
				x="18" 
				y="4" 
				z="0" 
				testing="false" 
				switched="8" 
				frogporttype="0" 
				addr1="7" 
				prev_id="rc1" 
				nr="0" desc="" 
				decid="" 
				blockid="" 
				routeids="[cb1+]-[sb4+],[cb1+]-[sb3+],[cb1+]-[sb2+],[cb1+]-[sb1+],[cb2+]-[sb4+],[cb2+]-[sb3+],[cb2+]-[sb2+],[cb2+]-[sb1+],[cb4-]-[sb4+],[cb4-]-[sb3+],[cb4-]-[sb2+],[cb4-]-[sb1+]" 
				manual="false" 
				outoforder="false" 
				operable="true" 
				staticuse="false" 
				subtype="default" 
				savepos="none" 
				dir="false" 
				swtype="default" 
				road="false" 
				show="true" 
				swapstraight="false" 
				rectcrossing="false" 
				iid="" 
				uidname="" 
				bus="0" 
				port1="0" 
				gate1="0" 
				inv="false" 
				singlegate="false" 
				accessory="false" 
				addr2="0" 
				port2="0" 
				gate2="0" 
				inv2="false" 
				actdelay="false" 
				syncdelay="false" 
				delay="0" 
				param1="0" 
				value1="1" 
				param2="0" 
				value2="1" 
				prot="D" 
				porttype="0" 
				tdiid="" 
				tdaddr="0" 
				tdport="0" 
				td="false" 
				fbR="" 
				fbG="" 
				fb2R="" 
				fb2G="" 
				fbOcc="" 
				fbOcc2="" 
				fbRinv="false" 
				fbGinv="false" 
				fb2Rinv="false" 
				fb2Ginv="false" 
				fbset="false" 
				fbusefield="false" 
				ctciid1="" 
				ctciid2="" 
				ctcuid1="" 
				ctcuid2="" 
				ctcbus1="0" 
				ctcbus2="0" 
				ctcaddr1="0" 
				ctcaddr2="0" 
				ctccmdon1="false" 
				ctccmdon2="false" 
				ctcflip1="true" 
				ctcflip2="true" 
				ctciidled1="" 
				ctciidled2="" 
				ctcbusled1="0" 
				ctcbusled2="0" 
				ctcaddrled1="0" 
				ctcaddrled2="0" 
				ctcportled1="0" 
				ctcportled2="0" 
				ctcgateled1="0" 
				ctcgateled2="0" 
				ctcasswitchled1="false" 
				ctcasswitchled2="false" 
				frogiid="" 
				buspol="0" 
				frogtimer="0" 
				addr0pol1="0" 
				port0pol1="0" 
				gate0pol1="0" 
				addr0pol2="0" 
				port0pol2="0" 
				gate0pol2="0" 
				addr1pol1="0" 
				port1pol1="0" 
				gate1pol1="0" 
				addr1pol2="0" 
				port1pol2="0" 
				gate1pol2="0" 
				frogaccessory="true" 
				frogswitch="false" 
				state="turnout" 
				wantedstate="turnout" 
				fieldstate="turnout">
				'''

	# Tag: 'tk'
	def get_tracks_nice_list(self, data, tag):
		# print(f"datos: {data}, tag: {tag}")
		items = data.getElementsByTagName(self.STATIC_ITEMS[4])
		for item in items:
			if tag == item.getAttribute('id'):
				track_ =( 'Item name: ' + item.getAttribute('id') 
							+ '\nType: ' + item.getAttribute('type') + '\nOrientation: ' + item.getAttribute('ori') 
			    	      	+ '\nX axis: ' + item.getAttribute('x') + '\nY axis: ' + item.getAttribute('y')
			    	      	+ '\nZ axis: ' + item.getAttribute('z') + '\nPrevious ID: ' + item.getAttribute('prev_id')
			             	+ '\nBlock ID: ' + item.getAttribute('blockid') + '\nSensor ID: ' + item.getAttribute('sensorid')
			  	          	+ '\nRoad: ' + item.getAttribute('road') + '\nRoute IDs: ' + item.getAttribute('routeids')
			   	          	+ '\nTknr: ' + item.getAttribute('tknr')
		      			  	)
				return track_
				'''
				<tk 
				type="straight" 
				id="tk20171112121319069" 
				x="5" 
				y="4" 
				z="0" 
				pre_move_x="9" 
				pre_move_y="4" 
				pre_move_z="0" 
				routeids="[sb4-]-[cb1+],[sb4-]-[cb3+],[sb4-]-[cb2+]" 
				blockid="sb4"/>
				'''

	# Tag: 'tx'
	def get_texts_nice_list(self, data, tag):
		items = data.getElementsByTagName(self.STATIC_ITEMS[5])
		for item in items:
			if tag == item.getAttribute('id'):
				tx_ =( 'Text name: ' + item.getAttribute('id') 
   			            + '\nText: ' + item.getAttribute('text') + '\nBlock: '+ item.getAttribute('block') 
   			            + '\nSliderval: '+ item.getAttribute('sliderval') + '\nOrientation: ' + item.getAttribute('ori')
   			            + '\nX axis: ' + item.getAttribute('x') + '\nY axis: ' + item.getAttribute('y')
   			            + '\nZ axis: ' + item.getAttribute('z') 
   			            )
				return tx_
				'''
				<tx 
				id="staging1" 
				text="Staging Area" 
				x="5" 
				y="0" 
				z="0" 
				block="" 
				prev_id="staging1" 
				desc="" 
				pointsize="0" 
				bold="true" 
				underlined="false" 
				border="false" 
				italic="false" 
				transparent="true" 
				mirror="false" 
				manualinput="false" 
				show="true" 
				reset="false" 
				clock="false" 
				webcam="false" 
				refresh="0" 
				ori="west" 
				iid="" 
				bus="0" 
				addr="0" 
				display="1" 
				speak="false" 
				cx="5" 
				cy="1" 
				sliderval="0" 
				html="false" 
				center="false" 
				fixed="false" 
				slider="false" 
				toggle="false" 
				slidermin="0" 
				slidermax="255"/>
				'''

	# Tag: 'bk'
	def get_block_nice_list(self, data, tag):
		items = data.getElementsByTagName(self.STATIC_ITEMS[6])
		for item in items:
			if tag == item.getAttribute('id'):
				block_ =( 'Block ID: ' + item.getAttribute('id') 
	    	                + '\nDescription: ' + item.getAttribute('desc') + '\nPlataform: '+ item.getAttribute('platform') 
	    	                + '\nState: ' + item.getAttribute('state') + '\nTerminal stataion? ' + item.getAttribute('terminalstation') 
	    	                + '\nMain line? ' + item.getAttribute('mainline') + '\nSignal: '+ item.getAttribute('signal') 
	    	                + '\nSignalR: ' + item.getAttribute('signalR') + '\nReset signal on reset? ' + item.getAttribute('resetsignalonexit') 
	    	                + '\nWait mode: ' + item.getAttribute('waitmode') + '\nAction: ' + item.getAttribute('action')
	    	                )
				return block_
				'''
				<bk 
				id="sb1" 
				x="5" 
				y="1" 
				z="0" 
				reserved="false" 
				entering="false" 
				managerid="" 
				fifoids="" 
				pre_move_x="9" 
				pre_move_y="1" 
				pre_move_z="0" 
				locid="" 
				state="open" 
				ori="east" 
				prev_id="sb1" 
				desc="" 
				len="0" 
				offsetplus="0" 
				offsetminus="0" 
				departdelay="0" 
				fifosize="0" 
				randomrate="10" 
				electrified="false" 
				gomanual="true" 
				acceptghost="false" 
				acceptident="false" 
				terminalstation="false" 
				wait="true" 
				road="false" 
				allowchgdir="true" 
				smallsymbol="false" 
				extstop="false" 
				allowbbt="true" 
				bbtfix="0" 
				mainline="false" 
				sleeponclosed="false" 
				freeblockonenter="false" 
				freeblockonenterplus="true" 
				freeblockonentermin="true" 
				allowaccessoncars="true" 
				centertrain="false" 
				secondnextblock4wait="false" 
				polarisation="true" 
				rearprotection="false" 
				commuter="yes" 
				show="true" 
				virtual="false" 
				slaveblocks="" 
				ttid="" 
				codesen="" 
				signal="sb1s" 
				wsignal="" 
				signalR="" 
				wsignalR="" 
				statesignal="" 
				openblocksignal="false" 
				openblockid="" 
				openblocksignalR="false" 
				openblockidR="" 
				speed="cruise" 
				exitspeed="cruise" 
				stopspeed="mid" 
				type="none" 
				nonewaittype="" 
				incline="0" 
				waitmode="random" 
				maxkmh="0" 
				minwaittime="1" 
				maxwaittime="5" 
				waittime="10" 
				mvscale="0" 
				mvdistance="0" 
				mvmph="false" 
				mvrecord="false" 
				evttimer="0" 
				evttimer2="0" 
				forceblocktimer="false" 
				selectshortestblock="false" 
				iid="" 
				addr="0" 
				port="0" 
				td="false" 
				tdV0="false" 
				tdlinkblocks="true" 
				typeperm="" 
				class="" 
				era="0" 
				masterid="" 
				controlcode="" 
				slavecode="" 
				server="infwABF34D30" 
				shunting="false" 
				embeddedfbplus="false" 
				embeddedfbmin="false">
				'''

	# Tag: 'sg'	
	def get_signals_nice_list(self, data, tag):
		items = data.getElementsByTagName(self.STATIC_ITEMS[7])
		for item in items:
			if tag == item.getAttribute('id'):
				signal_ = ( 'Signal: ' + item.getAttribute('id') 
								+ '\nDescription: ' + item.getAttribute('desc')
            	                + '\nInterface: ' + item.getAttribute('iid') + '\nAddress: ' + item.getAttribute('addr1')
								+ '\tPort: ' + item.getAttribute('port1') + '\nType: ' + item.getAttribute('type') 
                                + '\nSignal: '+ item.getAttribute('signal')  + '\nState: ' + item.getAttribute('state')
            	                + '\nAspects: ' + item.getAttribute('aspects') + '\nOrientacion: '+ item.getAttribute('ori') 
            	                + '\nInvert? ' + item.getAttribute('inv') + '\nX axis: ' + item.getAttribute('x')  
            	                + '\nY axis: ' + item.getAttribute('y') + '\nZ axis: ' + item.getAttribute('z')
            	                + '\nOperable?: ' + item.getAttribute('operable')+ '\nManual?: ' + item.getAttribute('manual')
            	                            )
				return signal_
				'''
            	<sg 
            	* type="light" 
            	* signal="main" 
            	* aspects="2" 
            	* id="sg1" 
            	* x="5" 
            	* y="3" 
            	* z="0" 
            	* addr1="5" 
            	* state="red" 
            	* manual="false" 
            	* aspect="0" 
            	* ori="east" 
            	porttype="0" 
            	prev_id="sg1" 
            	nr="0" 
            	* desc="Talleres bucle 1" 
            	decid="" 
            	blockid="" 
            	sensorid="" 
            	freeid="" 
            	blankid="" 
            	blankaspects="" 
            	road="false" 
            	oppositeid="false" 
            	routeids="" 
            	manualreset="true" 
            	* operable="true" 
            	accnr="0" 
            	show="true" 
            	showid="true" 
            	sod="true" 
            	resetid="" 
            	* iid="DCCppSerial" 
            	uidname="" 
            	bus="0" 
            	addr2="0" 
            	addr3="0" 
            	addr4="0" 
            	port1="3" 
            	port2="0" 
            	port3="0" 
            	port4="0" 
            	gate1="0"
            	gate2="0" 
            	gate3="0" 
            	gate4="0" 
            	prot="N" 
            	symbolprefix="" 
            	dwarf="false" 
            	usesymbolprefix="false" 
            	usepatterns="0" 
            	* inv="false" 
            	pair="false" 
            	asswitch="false" 
            	actdelay="false" 
            	delay="0" 
            	accessory="true" 
            	cmdtime="0" 
            	dim="10" 
            	bri="100" 
            	param="0" 
            	ctciid1="" 
            	ctciid2="" 
            	ctciid3="" 
            	ctcuid1="" 
            	ctcuid2="" 
            	ctcuid3="" 
            	ctcbus1="0" 
            	ctcbus2="0" 
            	ctcbus3="0" 
            	ctcaddr1="0" 
            	ctcaddr2="0" 
            	ctcaddr3="0" 
            	ctcflip1="false" 
            	ctcflip2="false" 
            	ctcflip3="false" 
            	ctciidled1="" 
            	ctciidled2="" 
            	ctciidled3="" 
            	ctcbusled1="0" 
            	ctcbusled2="0" 
            	ctcbusled3="0" 
            	ctcaddrled1="0" 
            	ctcaddrled2="0" 
            	ctcaddrled3="0" 
            	ctcportled1="0" 
            	ctcportled2="0" 
            	ctcportled3="0" 
            	ctcgateled1="0" 
            	ctcgateled2="0" 
            	ctcgateled3="0" 
            	ctcasswitchled1="false" 
            	ctcasswitchled2="false" 
            	ctcasswitchled3="false" 
            	ctcOutput="" 
            	ctcColorRed="0" 
            	ctcColorYellow="0" 
            	ctcColorGreen="0" 
            	ctcColorWhite="0" 
            	ctcColorBlank="0" 
            	green="0" 
            	red="0" 
            	yellow="0" 
            	white="0" 
            	blank="0" 
            	greennr="0" 
            	rednr="0" 
            	yellownr="0" 
            	whitenr="0" 
            	blanknr="0" 
            	a1nr="0" 
            	a2nr="0" 
            	a3nr="0" 
            	a4nr="0" 
            	a5nr="0" 
            	aspectnames=""
            	/>
    			'''

	# Tag: 'fb'
	def get_sensors_nice_list(self, data, tag):
		items = data.getElementsByTagName(self.STATIC_ITEMS[8])
		for item in items:
			if tag == item.getAttribute('id'):
				fb_ = ('Sensores: ' + item.getAttribute('id') + '\nDescription: ' + item.getAttribute('desc')
            	        + '\nInterface: ' + item.getAttribute('iid')  + '\nAddress: ' + item.getAttribute('addr') 
            	        + '\nState? ' + item.getAttribute('state') + '\nType? ' + item.getAttribute('fbtype')
            	        + '\nRegister trigger: ' + item.getAttribute('regtrigger')
            	        + '\nBlock: ' + item.getAttribute('blockid')  
            	        + '\nTimer: ' + item.getAttribute('timer') + ' x 100ms'
            	        + '\ncontador: ' + item.getAttribute('counter') + '\nRoad? '+ item.getAttribute('road') 
            	        + '\nCurve? '+ item.getAttribute('curve') + '\nOrientacion: '+ item.getAttribute('ori') 
            	        + '\nX axis: ' + item.getAttribute('x')  + '\nY axis: ' + item.getAttribute('y') 
            	        + '\nZ axis: ' + item.getAttribute('z')
            	        + '\nOperable? ' + item.getAttribute('operable')
            	        )
				return fb_
            

				'''
				<fb 
				* id="irb1norte" 
				x="6" 
				y="1" 
				z="0" 
				* state="true" 
				identifier="" 
				gpssid="0" 
				shortcut="false" 
				* counter="1" 
				wheelcount="0" 
				carcount="0" 
				countedcars="0" 
				bididir="0" 
				val="0" 
				load="0" 
				regval="0" 
				maxload="0" 
				ori="south"
				baseaddr="0" 
				regunits="0" 
				* addr="1" 
				offset="" 
				bus="0" 
				* fbtype="3" 
				rfid="0" 
				prev_id="fb1" 
				* desc="IR Bucle 1 Norte" 
				decid="" 
				show="true" 
				showid="true" 
				* road="false" 
				* curve="false" 
				ignoresamestate="false" 
				* blockid="IR B1 Norte" 
				routeids="" 
				accnr="0" 
				* timer="7" 
				zerocodedelay="0" 
				* operable="true" 
				generated="false" 
				iid="DCCppSerial" 
				uidname="" 
				reg0="0" 
				reg1="0" 
				reg2="0" 
				reg3="0" 
				reg4="0" 
				reg5="0" 
				reg6="0" 
				reg7="0" 
				threshold="1" 
				cutoutbus="0" 
				cutoutaddr="0" 
				subscribe="" 
				* regtrigger="4" 
				activelow="false" 
				resetwc="false" 
				ctciid="DCCppSerial" 
				ctcbus="0" 
				ctcaddr="0" 
				ctcport="0" 
				ctcgate="0" 
				ctcasswitch="false" 
				ctcOutput="" 
				ctcColorOn="0" 
				ctcColorOff="0" 
				gpsx="0" 
				gpsy="0" 
				gpsz="0" 
				gpstolx="0" 
				gpstoly="0" 
				gpstolz="0"
				/>
				'''	

	# Tag: 'co'
	def get_outputs_nice_list(self, data, tag):
		items = data.getElementsByTagName(self.STATIC_ITEMS[9])
		for item in items:
			if tag == item.getAttribute('id'):
				output_ = ('Output: ' + item.getAttribute('id') + '\nDescription: ' + item.getAttribute('desc')
            	            + '\nInterface: ' + item.getAttribute('iid')  + '\nAddress: ' + item.getAttribute('addr') 
            	            + '\nState? ' + item.getAttribute('state') 
            	            + '\nValue: ' + item.getAttribute('value') + '\nAccesory) ' + item.getAttribute('accessory')  
            	            + '\nBlock: ' + item.getAttribute('blockid')  + '\nTimer: ' + item.getAttribute('timer') + ' x 100ms'
            	            + '\ncontador: ' + item.getAttribute('counter') + '\nRoad? '+ item.getAttribute('road') 
            	            + '\nCurve? '+ item.getAttribute('curve') + '\nOrientacion: '+ item.getAttribute('ori') 
            	            + '\nX axis: ' + item.getAttribute('x')  + '\nY axis: ' + item.getAttribute('y') 
            	            + '\nZ axis: ' + item.getAttribute('z') + '\nShow? ' + item.getAttribute('show')
            	            + '\nOperable? ' + item.getAttribute('operable')
            	            )
				return output_

				'''
				<co 
				svgtype="1" 
				id="co1" 
				x="5" 
				y="8" 
				z="0" 
				value="1" 
				state="off" 
				valueoff="0" 
				porttype="0" 
				prev_id="co1" 
				nr="0" desc="" 
				decid="" 
				show="true" 
				showid="true" 
				svgacctype="false" 
				blockid="" 
				sensorid="" 
				routeids="" 
				grpid="" 
				tristate="false" 
				toggleswitch="true" 
				operable="true" 
				showbri="true" 
				iid="DCCppSerial" 
				bus="0" 
				uidname="" 
				addr="0" 
				port="0" 
				gate="0" 
				param="0" 
				paramoff="0" 
				delay="0" 
				publish="" 
				subscribe="" 
				cmd_on="" 
				cmd_off="" 
				prot="N" 
				inv="false" 
				blink="false" 
				colortype="false" 
				plancolor="false" 
				native="false" 
				asswitch="false" 
				accessory="true" 
				redChannel="0" 
				greenChannel="0" 
				blueChannel="0" 
				whiteChannel="0" 
				white2Channel="0" 
				brightnessChannel="0">
				<color 
				red="0" 
				green="0" 
				blue="0" 
				white="0" 
				white2="0" 
				saturation="254" 
				rgbType="0" 
				brightness="0" 
				id=""/>
				</co>
				'''

	def get_nice_rocrail_ini(self, data_ini):
		
		file = xml.dom.minidom.parse('/home/peyu/snap/Rocrail/demo/rocrail.ini')
		datas = file.getElementsByTagName('rocrail')

		for data in datas:
			a = data.getAttribute('planfile')
			print("planfile:" + a)
			
	def getText(self, nodelist):
		rc = []
		for node in nodelist:
		    if node.nodeType == node.TEXT_NODE:
		    	print(node.data)
		    	rc.append(node.data)
		    	a = ''.join(rc)
		    	print("Class_list_getText", a)
		    	return a


