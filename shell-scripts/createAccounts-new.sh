#!/usr/bin/env bash

# Needs number of accounts to be created as first parameter
# Requires: curl, grep
set +e
# Admin Login
#curl -X POST -H "Content-Type: application/json" -d '{"name": "admin","password": "222222"}' http://localhost:8080/account/adminlogin > temp.txt

# Extract Login UUID from response
#loginId=$(grep -zoP '"id":\s*\K[^\s,]*(?=\s*,)' temp.txt)
#echo "LoginID: $loginId"
#rm temp.txt

# Create User Accounts
for ((i = 1 ; i <= $1 ; i++)); do
    payload="{\"userName\": \"user$i\", \"password\": \"user$i\", \"gender\": 1, \"email\": \"user$i@test.com\", \"documentType\": 1, \"documentNum\": 1}"
    curl -X POST -H "Content-Type: application/json" -d "$payload" http://localhost:8080/api/v1/userservice/users/register
done
set -e
