#AWS Operational Scripts

##DynamoDB Scripts

### Delete a table in a region of your choice

This script uses user inputs for a 'region' and Dynamo 'table' name to execute the boto `delete_table` method.

	def delete_table(self):
	    print("Checking if region exists...")
	    for n in Dynamo.region_name:
	        if region == n:
	            region_state = True
	            print("We found region: '%s'" % region)
	            break
        if region_state == True:
            client = boto3.client('dynamodb', region_name = '%s' % self.region)
            print ("Checking if table exists...")
            try:
                description = client.describe_table(TableName = '%s' % self.tablename)
                table_state = True
                print('Table exists!')
            except Exception as e:
                if "Requested resource not found: Table" in str(e):
                    table_state = False
                    print("Table does not exist")
        else:
            print("Please validate the region before proceeding!")

        if region_state == True & table_state == True:
            print("Deleting Table!")
            delete_response = client.delete_table(TableName = '%s' % tablename)
            waiter = client.get_waiter('table_not_exists')
            if waiter == True:
                print("Table deleted!")

This script will also make sure that the region and table name are valid. If and only if both the region and table names are validated will the `delete_table` method be executed. 

Validating the 'table name' field is done with the `describe_table` method. Using the region input, boto will call Dynamo for information regarding the inputted table name. 

###Increase Dynamo table read and/or write capacity if existing capacity is approaching 100 percent full

 