#!/bin/bash
export DATAGEN_HOME=/home/ubuntu/datagen_afterCB
echo $DATAGEN_HOME
drop=true
run=true
#read -a sizes <<< $1
sizes=( "$@" )
for s in "$sizes[@]"
do
	        echo $s;
done
	dataset_prefix="wisconsin_dataset"
	dataset_distributions=("40960")
	datagen_prefix="wisconsin_dataset"
	NC=10.16.229.110
	CC=10.16.229.110
	PORT=10001
	ClearCache=false
	echo "http://$CC:19002/query/service"
	if [ $drop != false ]
	then
		  curl -v  --data-urlencode statement="
		  drop dataverse unlimitedMemory if exists;
		  create dataverse unlimitedMemory;
		  USE unlimitedMemory;

		  CREATE TYPE wisconsin_unlimitedMemory2 AS {
		    unique1: int,
		      unique2: int,
		       two: int,
		        four:int,
			 ten:int,
			  twenty:int,
			   onePercent:int,
			    tenPercent:int,
			     twentyPercent:int,
			       fiftyPercent: int,
			        unique3:int,
				 evenOnePercent:int,
				  oddOnePercent:int,
				    stringu1: string,
				      stringu2: string,
				       string4:string,
				         integer1:int
				 };

				 CREATE TYPE wisconsin_unlimitedMemory AS {
				     unique1: int,
				         unique2: int,
					         two: int,
						         four:int,
							         ten:int,
								         twenty:int,
									         onePercent:int,
										         tenPercent:int,
											         twentyPercent:int,
												     fiftyPercent: int,
												             unique3:int,
													             evenOnePercent:int,
														             oddOnePercent:int,
															             stringu1: string,
																         stringu2: string,
																	         string4:string
																	 };
																	 " "http://$CC:19002/query/service"
	fi
	 echo "drop done"
	 if [ $run != false ]
	 then

		 for i in "${dataset_distributions[@]}"
		 do 
					        #         for round in {1..100..10}
						      #          do
						             #          declare -i START=$round
							             #         declare -i END=$((round + 9))
								                       
								       for ((ds=1; ds<=5; ds++  ));
									         do
											    curl -v  --data-urlencode statement="USE unlimitedMemory;
											       drop dataset "$dataset_prefix"_"$i"__ds"$ds" if exists;
											          CREATE DATASET "$dataset_prefix"_"$i"_ds"$ds"(wisconsin_unlimitedMemory)
												            PRIMARY KEY unique2
													                            with {\"storage-block-compression\": {\"scheme\": \"none\"}};
																     CREATE INDEX u1Index on "$dataset_prefix"_"$i"_ds"$ds"(unique1);
create feed  "$dataset_prefix"_"$i"_"$ds"_feed  with {
            \"adapter-name\": \"localfs\",
	                \"path\":\"10.16.229.110:///home/dbis-nuc10/DBIS/data/wisconschedular40gb.adm\",
			            \"type-name\": \"wisconsin_unlimitedMemory\",
				                \"format\": \"adm\"
								            };

									          USE unlimitedMemory;
										        connect feed "$dataset_prefix"_"$i"_"$ds"_feed to dataset "$dataset_prefix"_"$i"_ds"$ds";" "http://$CC:19002/query/service"

											      curl -v  --data-urlencode statement="USE unlimitedMemory;
											            start feed "$dataset_prefix"_"$i"_"$ds"_feed ;" "http://$CC:19002/query/service"
																										          done
																											            sleep 1m
																												              done
											       fi

											       if [ $ClearCache != false ]
											       then
												        echo "ClearCache"
													 curl -v  --data-urlencode statement="USE unlimitedMemory;
													  CREATE DATASET clear_cache (wisconsin_unlimitedMemory)
													           PRIMARY KEY unique2
														                   with {\"storage-block-compression\": {\"scheme\": \"none\"}};

																   create feed clear_cache_feed  with {
																           \"adapter-name\": \"socket_adapter\",
																	           \"sockets\": \""$NC":"$PORT"\",
																		           \"address-type\": \"IP\",
																			           \"type-name\": \"wisconsin_unlimitedMemory\",
																				           \"format\": \"adm\"
																					         };
																						 USE unlimitedMemory;
																						  connect feed clear_cache_feed to dataset clear_cache;" "http://$CC:19002/query/service"
																						   curl -v  --data-urlencode statement="USE unlimitedMemory;
																						     start feed clear_cache_feed ;" "http://$CC:19002/query/service" 
																						       java -jar /home/ubuntu/datagen_afterCB/target/wisconsin-datagen.jar writer=asterixdb workload=wisconsin_fixed_record_size.json  cardinality=99999999 filesize=80000 
																						         curl -v  --data-urlencode statement="USE unlimitedMemory; stop feed  clear_cache_feed; drop feed  clear_cache_feed;" "http://$CC:19002/query/service"
																							 fi
