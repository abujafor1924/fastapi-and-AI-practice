Based on your CV, I would rate you as a Junior-to-Mid-Level Django Backend Developer. You have good practical experience with Django, DRF, Docker, Celery, Redis, PostgreSQL, and AI integrations. Your biggest gap appears to be computer science fundamentals, database optimization, Django internals, and system design concepts—which is exactly what interviewers often test.

CV Review

Strengths

✅ Real-world Django projects

✅ Docker, Nginx, Gunicorn deployment experience

✅ Celery + Redis experience

✅ PostgreSQL experience

✅ AI integration (OpenAI, Gemini)

✅ Multiple client projects

✅ React experience

Weaknesses

1. Your English has several grammatical mistakes. This can hurt client interviews.


2. Some project descriptions are too short and don't show impact.


3. You mention AWS, but be prepared for AWS questions. Many interviewers will ask about EC2, S3, IAM, Load Balancers, etc.


4. Your education section comes before your technical skills and experience. For experienced developers, experience should usually be higher.


5. There are typos:

"Advace Django API" → "Advanced Django API"

"process" → "process"

"Tread App" → If you mean trade, use "Trade"




Overall Rating

Django: 7/10

DRF: 7/10

PostgreSQL: 5/10

Docker: 6/10

AWS: 4/10

System Design: 4/10

English Communication: 5/10


Overall: 6.5/10


---

100 Interview Questions You Should Be Able to Answer

Python (1-20)

1. What are Python decorators?
A decorator is a function that modifies or extends the behavior of another function without changing its source code. It is commonly used for logging, authentication, caching, and validation.

2. What is a generator?
A generator is a special function that uses yield to produce values one at a time instead of returning them all at once. It saves memory and is ideal for processing large datasets.



3. Generator vs Iterator?
Every generator is an iterator, but not every iterator is a generator.


4. What is a context manager?
A context manager manages resources automatically using the with statement. It ensures proper setup and cleanup even if an exception occurs.


5. What is GIL?
The GIL is a mutex in CPython that allows only one thread to execute Python bytecode at a time. It simplifies memory management but limits true parallel execution for CPU-bound tasks.


6. List vs Tuple?
Lists are mutable, while tuples are immutable. Tuples are faster and use less memory, whereas lists are suitable when data needs to be modified.


7. Deep copy vs Shallow copy?
A shallow copy copies only the outer object, while nested objects remain shared. A deep copy recursively copies all nested objects, creating a completely independent copy.


8. What are Python comprehensions?
Comprehensions provide a concise syntax for creating lists, dictionaries, sets, and generators from iterable objects.


9. What is monkey patching?
Monkey patching means dynamically modifying classes or objects at runtime by replacing or adding methods or attributes.


10. What is duck typing?
Duck typing means Python determines an object's suitability by its behavior (methods and attributes) rather than its actual type.


11. What is method overloading?
Python does not support traditional method overloading. The latest method definition overrides previous ones. Flexible arguments like *args, default parameters, or type checking are used instead.


12. What is method overriding?
Method overriding allows a subclass to provide a different implementation of a method inherited from its parent class. It is a key feature of polymorphism.


13. What is MRO?
MRO defines the order in which Python searches parent classes for methods and attributes. It ensures consistent behavior in multiple inheritance.



14. Explain *args and **kwargs.
*args allows a function to accept any number of positional arguments as a tuple, while **kwargs accepts any number of keyword arguments as a dictionary.


15. What is a closure?
A closure is an inner function that retains access to variables from its enclosing scope, even after the outer function has returned.


16. What are lambda functions?
A lambda function is an anonymous, single-expression function. It is commonly used with functions like map(), filter(), and sorted().


17. What is multithreading?
Multithreading enables multiple threads within a single process. It is most effective for I/O-bound tasks but is limited for CPU-bound work by the GIL.


18. What is multiprocessing?
Multiprocessing runs tasks in separate processes, allowing true parallel execution and making it suitable for CPU-bound workloads.


19. What is async/await?
async defines a coroutine, and await pauses its execution until another asynchronous operation completes. This improves efficiency for I/O-bound applications.




20. What are dataclasses?
A dataclass is a Python feature that automatically generates methods such as __init__, __repr__, and __eq__ for classes that primarily store data, reducing boilerplate code.





---

Django (21-40)

21. Explain the Django request lifecycle.
Django receives the request through WSGI or ASGI, processes middleware, finds the correct URL, executes the view, interacts with the database if needed, returns a response, processes response middleware, and finally sends the response to the client.



22. What is WSGI?
WSGI is a standard interface that allows synchronous Django applications to communicate with web servers like Gunicorn or uWSGI.


23. What is ASGI?
ASGI is the asynchronous version of WSGI that supports async views, WebSockets, and long-running connections.


24. Middleware in Django?
Middleware is a component that processes requests before views execute and processes responses before they are sent to the client.

25. Signals?
Signals allow Django applications to execute code automatically when certain events occur, such as saving or deleting a model.




26. Custom User Model?
A Custom User Model extends or replaces Django's default user model to add custom fields and authentication behavior.


27. Model Managers?
Model Managers provide custom database query methods and control how model objects are retrieved.


28. Generic Views?
Generic Views reduce code duplication by providing reusable views for common CRUD operations.


29. CBV vs FBV?
Function-Based Views are simple and easy to understand, while Class-Based Views provide code reuse, inheritance, and built-in generic functionality.


30. Authentication vs. authorization?
Authentication verifies the user's identity, while authorization determines what resources the authenticated user can access.


31. Session Authentication?
Session Authentication stores the user's session on the server and uses a session ID stored in the browser cookie to authenticate future requests.


32. JWT Authentication?
JWT Authentication uses signed tokens instead of server-side sessions, making it ideal for REST APIs and mobile applications.


33. CSRF?
CSRF protects authenticated users from unauthorized requests by requiring a unique CSRF token with unsafe HTTP requests like POST, PUT, PATCH, and DELETE.


34. CORS?
CORS is a browser security mechanism that controls whether a web application can access resources from a different origin.


35. What is ORM?
Django ORM allows developers to interact with the database using Python objects instead of writing raw SQL queries.



36. What is migration?
Migrations are Django's way of creating and applying database schema changes in a version-controlled manner.


37. Why use Django over Flask?
Django provides built-in features like the ORM, authentication, admin panel, and security, making it suitable for larger applications, while Flask offers more flexibility for smaller or highly customized projects.


38. What is Django Admin?
Django Admin is an automatically generated interface that allows administrators to manage application data without building custom admin pages.


39. What is caching?
Caching improves application performance by storing frequently used data in memory, reducing repeated database queries and computation.


40. How do you optimize Django performance?
I optimize Django applications by reducing database queries with select_related() and prefetch_related(), using caching, indexing frequently queried fields, paginating large datasets, optimizing templates, serving static files efficiently, and monitoring performance with profiling tools.




---




Django ORM (41-55)

41. What is the N+1 Query Problem?
The N+1 Query Problem happens when one query retrieves a list of objects and additional queries are executed for each related object. It can significantly slow down applications and is usually solved with select_related() or prefetch_related().



42. select_related() vs prefetch_related()?
select_related() performs a SQL JOIN and is used for ForeignKey or OneToOne relationships, while prefetch_related() performs separate queries and combines the results in Python, making it suitable for ManyToMany and reverse ForeignKey relationships.


43. annotate() vs aggregate()?
annotate() adds calculated values to each object in a queryset, whereas aggregate() calculates a single summary value for the entire queryset.


44. filter() vs exclude()?
filter() retrieves objects that match the given conditions, while exclude() retrieves objects that do not match those conditions.


45. What is Q()?
Q() objects allow complex queries with AND, OR, and NOT conditions, making query construction more flexible.


46. What is F()?
F() expressions allow operations on database fields without fetching them into Python, improving performance and helping prevent race conditions.


47. How do you count queries?
I usually use Django Debug Toolbar to inspect database queries during development. Alternatively, I can check connection.queries to see the executed SQL queries.



48. What is lazy evaluation?
QuerySets in Django are lazily evaluated, meaning the SQL query is executed only when the data is actually needed.


49. What is queryset caching?
After a QuerySet is evaluated, Django caches its results, so subsequent access to the same QuerySet does not trigger another database query unless a new QuerySet is created.


50. exists() vs count()?
Use exists() when you only need to know whether at least one record exists because it is generally more efficient. Use count() when you need the exact number of matching records.


51. get() vs filter()?
get() returns a single object and raises an exception if zero or multiple objects are found, while filter() always returns a QuerySet that may contain zero, one, or many objects.


52. What are transactions?
Transactions group multiple database operations into a single unit of work. Using transaction.atomic(), either all operations succeed or all are rolled back if an error occurs.


53. What is select_for_update()?
select_for_update() locks selected rows during a transaction, preventing other transactions from modifying them until the lock is released.


54. How do indexes work?
Database indexes speed up searches and filtering by creating a data structure that allows faster lookups. They improve read performance but can slightly slow down inserts and updates because the index must also be maintained.


55. How do you optimize slow queries?
To optimize slow queries, I reduce unnecessary database hits with select_related() and prefetch_related(), add appropriate indexes, fetch only the required data, use caching, analyze query execution plans with explain(), and monitor SQL queries using tools like Django Debug Toolbar.




---

PostgreSQL (56-70)

56. Primary Key?
A Primary Key is a column (or columns) that uniquely identifies each row in a table.


57. Foreign Key?
A foreign key creates a relationship between tables.


58. Unique Constraint?
A UNIQUE constraint ensures that all values in a column are different.


59. Index?
An index makes SELECT faster but INSERT/UPDATE slightly slower.


60. Composite Index?
A Composite Index is an index on multiple columns.
Composite Index = One index + Multiple columns.


61. Explain JOIN.
JOIN combines related data from multiple tables.

62. INNER JOIN?
Returns only matching rows from both tables.


63. LEFT JOIN?
Returns all rows from the left table and matching rows from the right table.


64. RIGHT JOIN?
Returns all rows from the right table and matching rows from the left table.


65. Full JOIN?
Returns all rows from both tables.


66. What is normalization?
Normalization organizes data to reduce redundancy and improve consistency.
Normalization removes duplicate data.


67. What is denormalization?
Denormalization improves speed by reducing JOINs.


68. What is EXPLAIN ANALYZE?
EXPLAIN ANALYZE shows the actual execution plan and performance of a query.


69. ACID properties?
ACID ensures reliable database transactions.


70. Database transaction?
A transaction is a group of SQL operations executed as a single unit.
Transaction = Multiple operations succeed together or fail together.




---

DRF (71-80)

71. What is DRF?
Django REST Framework (DRF) is a powerful toolkit built on Django for developing RESTful APIs quickly and securely.


72. Serializer?
Serializer in DRF plays the same role as Forms in Django, but for APIs.



73. ModelSerializer?
A ModelSerializer is a shortcut version of Serializer that automatically generates fields and validators from a Django model.



74. ViewSet?
ViewSet combines multiple API views into one class, making APIs cleaner and easier to maintain.


75. Router?
A Router automatically generates URL patterns for ViewSets.


76. Permission classes?
Authentication identifies the user, while Permission determines what the user is allowed to do.


77. Authentication classes?
Authentication answers "Who are you?", while Permission answers "What are you allowed to do?"


78. Pagination?
Pagination improves API performance by returning data in manageable chunks instead of sending everything at once.


79. Throttling?
Throttling protects APIs by limiting request rates and preventing excessive traffic.


80. API versioning?
API Versioning ensures backward compatibility, allowing old clients to continue working while new features are introduced.




---

Celery & Redis (81-87)

81. Why use Celery?
Celery is a distributed task queue used to execute time-consuming tasks asynchronously in the background.
Instead of making users wait for long operations, Celery moves those tasks to a worker process while the application responds immediately.



82. What is a task queue?
A task queue decouples task execution from the user request, improving responsiveness and scalability.


83. Redis vs. database?
Redis is optimized for speed, while databases are optimized for durable data storage.


84. Celery Beat?
Celery Beat schedules periodic tasks, similar to cron jobs but integrated with Celery.


85. Retry mechanisms?
Retry mechanisms increase reliability by automatically re-executing failed tasks after a delay.


86. Worker process?
A Celery Worker continuously consumes tasks from the queue and executes them independently of the web server.


87. Background processing examples?
Background processing keeps applications responsive by moving heavy or slow operations outside the request-response cycle.




---

Docker & Deployment (88-94)


88. What is Docker?
Docker is a containerization platform that packages an application along with its dependencies, libraries, and configuration into a Container.
This ensures the application runs consistently across development, testing, and production environments.



89. Docker Image vs Container?
An Image is a blueprint, while a Container is the running application created from that blueprint.


90. Dockerfile?
A Dockerfile automates the creation of Docker Images using a sequence of instructions.


91. Docker Compose?
Docker Compose simplifies multi-container application management using a single YAML configuration file.


92. Nginx?
Nginx sits in front of Django, handling client requests efficiently before forwarding them to Gunicorn.


93. Gunicorn?
Gunicorn is the production WSGI server that executes Django applications and handles incoming HTTP requests.


94. CI/CD pipeline?
CI/CD (Continuous Integration & Continuous Deployment/Delivery) automates software building, testing, and deployment.




---

AWS & System Design (95-100)

95. What is EC2?
EC2 (Elastic Compute Cloud) is AWS's virtual server service.
It allows you to deploy applications on scalable cloud servers.



96. What is S3?
S3 is highly durable object storage used for storing static assets, media files, and backups.


97. What is IAM?
IAM (Identity and Access Management) controls who can access AWS resources and what actions they can perform.


98. What is a Load Balancer?
A Load Balancer improves availability and performance by distributing traffic across multiple servers.


99. How would you scale a Django application?
Scale Django by distributing traffic, caching data, offloading background tasks, and horizontally adding application servers.


100. Design a URL Shortener system.
A URL shortener maps unique short codes to original URLs, using caching and indexing to achieve fast redirection at scale.



If you can confidently answer 80+ of these questions, you'll be in a strong position for most Django Backend Developer interviews. Looking at your background, I'd prioritize questions 21-55 and 88-100 first, because those are the areas interviewers are most likely to challenge you on.



Good — now I’ll upgrade this to Mid + Senior level Django Backend interview questions based on your CV and gaps.
These questions are what companies use to filter real backend engineers, not beginners.

🚀 Mid + Senior Django Backend Interview Questions (100)
🧠 Python Advanced (1–15)
How does Python memory management work?
Python manages memory using a private heap where all objects are stored. The memory manager handles allocation and deallocation automatically using reference counting and garbage collection.
What is reference counting in Python?
Every object has a counter that tracks how many references point to it. When the count becomes zero, the memory is freed immediately.
How does garbage collection work in Python?
Python uses a cyclic garbage collector to clean up objects that reference each other but are no longer reachable.
What are circular references?
A circular reference happens when two or more objects reference each other, forming a cycle.
How does Python handle memory leaks?
Python reduces leaks via:
Reference counting
Garbage collector for cycles
gc module for debugging
Weak references (weakref)
But leaks still happen due to:
global caches
circular references with __del__
unclosed resources
Difference between __str__ and __repr__?
__str__ → user-friendly output
__repr__ → developer/debug-friendly (detailed, unambiguous)

What are metaclasses in Python?
A metaclass is a “class of a class”. It controls how classes are created.
Default metaclass: type
When would you use a metaclass?
Used when you need to:
enforce rules on class creation
register classes automatically
modify class attributes globally
frameworks (Django ORM, Pydantic)
How does Python import system work internally?
Python:
Checks sys. modules (cache)
Looks in built-in modules
Searches sys. path
Loads module
Executes module code
Stores it in cache
What is module caching?
Once a module is imported, Python stores it in sys. modules. Future imports reuse the same object instead of reloading.
How does Python handle variable scope resolution?
Python uses the LEGB rule:
Local
Enclosing
Global
Built-in
What are closures used for in real systems?
A closure is a function that remembers variables from its outer scope.
Used in:
decorators
callbacks
function factories
authentication wrappers

Explain descriptor protocol in Python.
Descriptors define how attribute access works using:
__get__
__set__
__delete__
Used in:
Django ORM fields
property()
class attributes
What is monkey patching and when is it dangerous?
Danger:
breaks maintainability
causes hidden bugs
affects global behavior
How does the Python async event loop work internally?
The event loop:
manages async tasks
runs coroutines
switches tasks when waiting (I/O)
uses cooperative multitasking
Core idea:
tasks pause on await
event loop resumes them later


⚙️ Django Internals (16–35)
Explain Django architecture internally.
How does Django handle the request → response cycle?
What happens when a Django server starts?
How does Django load settings?
What is Django app registry?
How do Django signals work internally?
Are Django signals synchronous or asynchronous?
What are the downsides of signals?
How does the Django middleware chain work?
What is middleware ordering impact?
What is WSGI in depth?
What is ASGI and why was it introduced?
Difference between WSGI and ASGI performance?
How does Django ORM connect to DB?
How does query compilation happen in ORM?
What is QuerySet evaluation delay?
What is lazy loading in Django ORM?
How does Django manage database connections?
What is connection pooling?
What happens during Django migration internally?

🧩 Django ORM Mastery (36–55)
What is QuerySet caching and when does it break?
How does select_related work internally?
How does prefetch_related work internally?
When does N+1 problem still occur despite optimization?
What is defer() and only()?
What is annotate() used for in analytics?
Difference between ORM aggregation vs SQL aggregation?
What is F() expression and real use cases?
What is Q() object and complex filtering?
What are subqueries in Django ORM?
How do you optimize slow ORM queries?
What is query plan (EXPLAIN ANALYZE)?
What is indexing strategy in Django models?
Composite indexes use cases?
What is database locking in Django ORM?
What is select_for_update() used for?
How do transactions work in Django?
What is atomic transaction block?
What is isolation level in DB transactions?
How do you prevent race conditions in Django?

🧱 Database & PostgreSQL (56–70)
What is MVCC in PostgreSQL?
How does PostgreSQL handle concurrency?
What is vacuum in PostgreSQL?
What causes slow queries in production?
How do indexes internally work (B-tree)?
When indexes hurt performance?
What is normalization vs denormalization in real systems?
When would you denormalize in production?
What is deadlock in databases?
How to detect deadlocks?
What is query execution plan?
Difference between clustered and non-clustered index?
What is sharding?
What is replication?
Master-slave vs multi-master architecture?

🚀 DRF (Django REST Framework) (71–82)
How does DRF serialization pipeline work?
What happens when serializer .is_valid() is called?
Custom validation flow in DRF?
How do ViewSets work internally?
Router vs manual URL mapping?
Permission system in DRF architecture?
Authentication flow in DRF?
Token vs JWT vs Session authentication?
How does pagination work internally?
How do throttling classes work?
How do you secure APIs in production?
How would you version a large API system?

⚡ Celery, Redis & Async Systems (83–90)
How does Celery distribute tasks?
What happens when a Celery worker crashes?
What is task idempotency?
How do retries work in Celery?
What is broker vs backend in Celery?
Redis persistence mechanisms?
When should you NOT use Celery?
How do you design background job systems at scale?

🐳 Docker & DevOps (91–96)
How does Docker networking work?
Difference between image layers?
How does container isolation work?
What is multi-stage Docker build?
How does Nginx act as reverse proxy?
Gunicorn worker types and tuning?

☁️ AWS & Production Systems (97–100)
How does EC2 auto scaling work?
S3 consistency model explained?
How do load balancers distribute traffic?
Design a scalable Django system for 1M+ users.

🔥 How to Use This List (Important)
Since you are currently Junior → Mid level, your roadmap should be:
Phase 1 (Must master first)
16–55 (Django + ORM + DB)
Phase 2 (Mid level strength)
71–90 (DRF + Celery + Redis)
Phase 3 (Senior preparation)
1–15 + 97–100 (System design + internals)

⚠️ Reality Check (Based on your CV)
To reach strong mid-level, you should focus on:
ORM optimization (N+1, indexing, query plans)
Django internals (middleware, lifecycle)
PostgreSQL deep concepts
System design (URL shortener, scalable APIs)

If you want, I can next:
👉 Turn this into a 30-day interview preparation roadmap
👉 Or do mock interview (I ask, you answer like real interview)
👉 Or explain each weak area (like ORM, N+1, system design) in Bangla
Just tell me 👍

