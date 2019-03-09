select id,count(1) from integratestagingdb.userdimension group by id having count(1) >1
