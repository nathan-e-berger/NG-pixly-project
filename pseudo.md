(Login/authentication isn’t required; any web user can do everything)

Users can view photos stored in the system

Users can add a JPG photo using an upload form and picking a file on their computer (you’ll need to learn how to allow image uploads!)

System will retrieve metadata from the photo (location of photo, model of camera, etc) and store it into the database (you’ll need to learn how to read the metadata from photos!)

Images themselves are stored to Amazon S3, not in the database (you’ll get to practice using AWS!)

Users can search image data from the EXIF fields (you can learn about PostgreSQL full-text search)

Users can perform simple image edits (for example): - turning color photos into B&W - adding sepia tones - reducing the size of the image - adding a border around the image