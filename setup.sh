#!/bin/bash

export AUTH0_DOMAIN='dev-1aweba2i.us.auth0.com'
export DATABASE_URL='postgresql://sansergi:123456@localhost:5432/casting_agency'
export AUTH0_AUDIENCE='Casting_Agency'
export AUTH0_CLIENT_ID='s3bxEkaLBmL9Sln0AIOMfotoSAOUDXJY'
export AUTH0_CLIENT_SECRET='MoWzhdACZ_H0zmb74tm_szQi75EhQhpsN7ov4EH5eEMZL483XhfqEpWVYFCwGGNK'
export ENV='development'
export FLASK_APP=app
export FLASK_DEBUG=True
export DB_HOST_TEST='localhost:5432'
export DB_USER_TEST='sansergi'
export DB_PASSWORD_TEST='123456'
export DB_NAME_TEST='casting_agency_test'
export AUTH0_CALLBACK_URL='http://127.0.0.1:8000/post-login'
export AUTH0_BASE_URL='https://dev-1aweba2i.us.auth0.com'
export executive_producer_token='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkVGZDEtblNKYUZyNlVSYW5qQnlXQyJ9.eyJpc3MiOiJodHRwczovL2Rldi0xYXdlYmEyaS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjA0Zjg0NWRhMjYwZjQwMDZhNzg2MDYxIiwiYXVkIjpbIkNhc3RpbmdfQWdlbmN5IiwiaHR0cHM6Ly9kZXYtMWF3ZWJhMmkudXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTYxNjY5MDM5NiwiZXhwIjoxNjE2Nzc2Nzk2LCJhenAiOiJzM2J4RWthTEJtTDlTbG4wQUlPTWZvdG9TQU9VRFhKWSIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.HaFv7Joz5uY6p9qd36rcp2Ku26Tyf0GXnlxrhPGPYPsaxOxHNnikWdjyClGKDGMLTkqW5nonxbOVjbtfgaTYHjuIMx8UW6GI0ngVT7aumloaS6w7nQ8Ja5uHTKAdfFfCQbgiIz9qiYHhK8OZRvSGEylOUA27vgeF2Z6N9Fhl6zfbk5EBr0IJOTaD9OWf2zDnlyZRrEj2Lz9bxdoaPgX1zgFZox35aoWvyL9u7gH4Gb6-k38Sm_QnjCxy8IEIDBnddDagT7nWViwb32d_-kBbruCnQeNG7C8KbqiDhkpfh29YU43dHwYtu-IipsO4YIMdroWbPHJF-ObvCKTUpxUrNQ'
export casting_director_token='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkVGZDEtblNKYUZyNlVSYW5qQnlXQyJ9.eyJpc3MiOiJodHRwczovL2Rldi0xYXdlYmEyaS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjA0Zjg0M2UzZjY0ODkwMDY4MTk2YTEyIiwiYXVkIjpbIkNhc3RpbmdfQWdlbmN5IiwiaHR0cHM6Ly9kZXYtMWF3ZWJhMmkudXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTYxNjY5MDM1MiwiZXhwIjoxNjE2Nzc2NzUyLCJhenAiOiJzM2J4RWthTEJtTDlTbG4wQUlPTWZvdG9TQU9VRFhKWSIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.X2tnrsuX5n31hR_Wp91vkhVxweV3ikTPVIc16NMQNre3NcEOzofKBT8AB8odUD4huXHNXIywYo_lfe4-6lWQmDzDI-8DYPhwzjyL0rUvBYlQSCLjhnqzf9eKKPQNmzIjpLoosRCmkwzfITmUhFTTtr9QvPHFj9YbYEkHr62mIkYWGsIVPUcuFzUUlkQE9z3__8iGc4oVahJdDSjRYqfMughGRn4O8rUfHa7lEy2ZU_gd_jb0zBhmVM2TyxTpyxTPhxR4YEmlrMyCGjS6TIC2mGPZkXLbQbppdM23aK6-qNhDz1AoX-GYhkijl276gjGsKXqpgexV_h9C1eduVw0Dxw'
export casting_assistant_token='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkVGZDEtblNKYUZyNlVSYW5qQnlXQyJ9.eyJpc3MiOiJodHRwczovL2Rldi0xYXdlYmEyaS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjA0ZjgzZDFhZGQ1YzgwMDZmZTM5ZGE5IiwiYXVkIjpbIkNhc3RpbmdfQWdlbmN5IiwiaHR0cHM6Ly9kZXYtMWF3ZWJhMmkudXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTYxNjY5MDI4OSwiZXhwIjoxNjE2Nzc2Njg5LCJhenAiOiJzM2J4RWthTEJtTDlTbG4wQUlPTWZvdG9TQU9VRFhKWSIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.ga8mOKf3MvB1mRZK5h2M8zCIGaaePW590EV60YhytradtINP4-TcsoRh32tqMppjw2cRvlkJ1guqVuFwDy-tsjiXl57AwGplPXu9i6bxbMGZjOeuji4hHfZS96hz4jbsRtM7pRTzVkeBh9LGVTAsssvcl3SnTUkBnEHkBOJDKnRQs6fr0HlI64x_QKaj9VfF2B-zWvTecd2RhIgQvcvLKjTZn8om5ACJtTFObdqPRKSmEkDGq1zpvrdtTHSbd9sh7r9iLrEm_58oTdKBntnYuFEzcm8yA1YiaClUT4XWbuJpN-MKv4KHJOZ_awP-QZDoP2cSf9nTO9mSdhv7v2RKig'