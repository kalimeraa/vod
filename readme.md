# VOD Application

### Genre Service API Architecture
- Runs on :5001
  - Admin CRUD API
    - [GET] => api/genres?page=1 (All genres)
    - [GET] => api/genres/{id} (Show a genre)
    - [POST] => api/genres (Create a genre)
    - [PUT] => api/genres/{id} (Update a genre)
    - [DELETE] => api/genres/{id} (Delete a genre)
  - Frontend API
    - [GET] => api/genres/{genre_slug}/films?page=1 (See genre's films)

### Content Service API Architecture
- Runs on :5000
    - Admin CRUD API
        - [GET] => api/films?page=1 (All films)
        - [GET] => api/films/{id} (Show a film)
        - [POST] => api/films (Create a film)
        - [PUT] => api/films/{id} (Update a film)
        - [DELETE] => api/films/{id} (Delete a film)
    - Frontend API
        - [GET] => api/films/genre/{genre_id}?page=1 (See genre's films)

## Stack
* **Flask**
* **PostgreSQL**
* **Redis**
* **Docker**

### Requirements for local installation

- Docker

### Installation
```
  chmod +x install.sh && ./install.sh
```

### Test Run
```
    on content-service directory
    docker-compose exec content-service bash
    pytest -s
    
    on genre-service directory
    docker-compose exec genre-service bash
    pytest -s
```

# Endpoints Collection
- Import vod.postman_collection.json to your postman, and you can easily see all endpoints 

### Questions
####1) What advantages do NumPy arrays offer over(nested) Python lists?
```
    1)Consumes less memory.
    2)Fast as compared to the python List.
    3)Convenient to use. For ex:
        # adding 5 to each element of Numpy array
        lst = [8,9,10]
        arr = np.array(ls)
        arr = arr + 5
```
####2)What is the difference between deep and shallow copy?
| Shallow Copy | Deep Copy |
| --- | --- |
| Shallow Copy stores the references of objects to the original memory address. | Deep copy stores copies of the object’s value. |
| Shallow Copy reflects changes made to the new/copied object in the original object. | Deep copy doesn’t reflect changes made to the new/copied object in the original object. |
| Shallow Copy stores the copy of the original object and points the references to the objects. | Deep copy stores the copy of the original object and recursively copies the objects as well.|
| Shallow copy is faster. | Deep copy is comparatively slower.|

```
# Python3 implementation of the Deep
# copy and Shallow Copy
from copy import copy, deepcopy
 
# Class of Car
class Car:
  def __init__(self, name, colors):
     
     self.name = name
     self.colors = colors
     
honda = Car("Honda", ["Red", "Blue"])
 
# Deepcopy of Honda
deepcopy_honda = deepcopy(honda)
deepcopy_honda.colors.append("Green")
print(deepcopy_honda.colors, \
      honda.colors)
 
# Shallow Copy of Honda
copy_honda = copy(honda)
 
copy_honda.colors.append("Green")
print(copy_honda.colors, \
      honda.colors)

// OUTPUT      
['Red', 'Blue', 'Green'] ['Red', 'Blue']
['Red', 'Blue', 'Green'] ['Red', 'Blue', 'Green']      
```
####3)How is Multithreading achieved in Python?
A thread is basically an independent flow of execution. A single process can consist of multiple threads.
Each thread in a program performs a particular task. For Example, when you are playing a game say FIFA on your PC,
the game as a whole is a single process, but it consists of several threads responsible for playing the music, taking
input from the user, running the opponent synchronously, etc. All these are separate threads responsible
for carrying out these different tasks in the same program.
Every process has one thread that is always running. This is the main thread. 
This main thread actually creates the child thread objects. 
The child thread is also initiated by the main thread.

```
import threading
  
def print_cube(num):
    """
    function to print cube of given num
    """
    print("Cube: {}".format(num * num * num))
  
def print_square(num):
    """
    function to print square of given num
    """
    print("Square: {}".format(num * num))
  
if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))
  
    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()
  
    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()
  
    # both threads completely executed
    print("Done!")
```

