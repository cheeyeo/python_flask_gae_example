### Simple FLASK APP

Super easy FLASK app created from the following tutorial:

https://realpython.com/python-web-applications/

The idea is to learn deployment to gcloud services.

### Running locally

```
python main.py
```

### Running on gcloud

* Create a new project on GCP App Engine

  Note the project id

* Login to gcloud from CLI:
  ```
  gcloud auth login
  ```

* Set the project ID:
  ```
  gcloud config set project <project id> (from step 1)
  ```

* Deploy:
  ```
  gcloud app deploy
  ```

  Will copy the files in current project directory

  The app.yaml file should specify the runtime and other configuration information

* To shutdown or delete app:
  ```
  gcloud projects delete <project id>
  
  ```

Note that logging will not always appear when running `gcloud app logs tail` in the CLI but will show up under the Log viewer in the Dashboard. This could be due to the changes between the Flexible and Standard Environment...

### More References

* (Google App Engine Documentation)[https://cloud.google.com/appengine/docs/python]