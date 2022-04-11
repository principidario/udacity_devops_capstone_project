export FLASK_APP=app
flask run

#Open another console where the file file.mp4 is located and run
curl -X POST -F file=@"file.mp4" http://localhost:5000/run
