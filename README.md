# BITS Laboratory Project, PHA-F366: 
3D MolVisualizer

### Mentors : [Dr. Murali Monohar Pandey](https://universe.bits-pilani.ac.in/pilani/pandeymm/profile)<br/><br/>



## Installation:
### Option 1: Conda
1. Install Miniconda, for your operating system, from [https://conda.io/miniconda.html](https://conda.io/miniconda.html)
2. `git clone https://github.com/vermasrijan/bits_lop_website`
3. `cd /path/to/bits_lop_website`
4. `conda env create -f environment.yml`
5. `conda activate lop` (or `source activate lop` for older versions of conda)
6.  `gunicorn web-app:app`
7. Go to `http://127.0.0.1:8000`
OR <br/>
6. `python3 web-app.py`
7. Go to `http://127.0.0.1:5000/`

### Option 2: Docker on local machine
1. `git clone https://github.com/vermasrijan/bits_lop_website`
2. `cd /path/to/bits_lop_website`
3. Open `Dockerfile` using any editor.
4. Comment the following line -> `CMD gunicorn web-app:app --bind 0.0.0.0:$PORT --reload`
5. Uncomment the follwoing 2 lines ->
```
EXPOSE 8080
ENTRYPOINT ["python3", "web-app.py"]
```
6. `docker build -t lop .`
7. `docker run -p 5000:5000 lop`
8. Go to `localhost:8080` OR `http://127.0.0.1:8080/`

1. Log in to Container Registry:

```
heroku container:login

```
2. Get code by cloning bits_lop_website:

```
git clone https://github.com/vermasrijan/bits_lop_website

```
3. Navigate to the app’s directory and create a Heroku app:

```
heroku create <Name_of_webapp>

```

4. Build the image and push to Container Registry:

```
heroku container:push web -a <Name_of_webapp>

```

5. Then release the image to your app:

```
heroku container:release web -a <Name_of_webapp>

```

Now open the app in your browser: 

```
heroku open

```
Go to ->
`<Name_of_webapp>.herokuapp.com`

## Reference:
1. [RDKit](https://www.rdkit.org/)
2. [3Dmol.js](https://3dmol.csb.pitt.edu/)
3. [Docker](https://www.docker.com/)
4. [Flask](https://flask.palletsprojects.com/en/1.1.x/)
5. [Heroku](https://www.heroku.com/)
