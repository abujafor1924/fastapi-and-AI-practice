# 🚀 Django Backend Interview Quick Reference Guide
## 200 Questions with 3-4 Line Answers for Interview Prep

---

## 🔷 PYTHON ADVANCED (1-15)

### 1. How does Python memory management work?
Python uses automatic memory management with a private heap containing objects. It uses reference counting for immediate deallocation and a generational garbage collector for circular references.

### 2. What is reference counting in Python?
Each object maintains a count of references pointing to it. When count reaches zero, memory is immediately freed. Simple and efficient but doesn't handle circular references.

### 3. How does garbage collection work in Python?
Complementary to reference counting, it detects and collects circular references using a generational approach with three generations. Objects surviving collections move to older generations.

### 4. What are circular references?
When two objects reference each other, forming a cycle. Reference counting can't free them because counts never reach zero, requiring the garbage collector to break cycles.

### 5. How does Python handle memory leaks?
Memory leaks occur when objects are unintentionally kept alive. Common causes: global variables, unclosed resources, circular references in containers. Use memory profilers and weakref module.

### 6. Difference between `__str__` and `__repr__`?
`__str__` returns user-friendly string representation, used by print() and str(). `__repr__` returns unambiguous representation for debugging, called by repr() and interactive console.

### 7. What are metaclasses in Python?
Metaclasses are classes of classes that define how a class behaves. They customize class creation, modify class attributes, and can enforce patterns. `type` is the default metaclass.

### 8. When would you use a metaclass?
Use for ORM frameworks, singleton patterns, automatic registration of subclasses, adding or validating class attributes, and implementing abstract base classes.

### 9. How does Python import system work internally?
Search in sys.path locations (built-in modules, .py files, zip files). Find module, compile if needed, create module object, execute code, and cache in sys.modules.

### 10. What is module caching?
Modules are stored in sys.modules dictionary after first import. Subsequent imports retrieve from cache, avoiding re-execution and improving performance significantly.

### 11. How does Python handle variable scope resolution?
Uses LEGB rule: Local → Enclosing → Global → Built-in. Variables in inner scopes can access outer variables but reassigning creates a new local variable unless using `nonlocal` or `global`.

### 12. What are closures used for in real systems?
Factory functions, decorators, callback functions, maintaining state in functional programming, and creating private variables. Used in web frameworks for request handlers.

### 13. Explain descriptor protocol in Python.
Protocol using `__get__`, `__set__`, `__delete__` methods. Controls attribute access. Used in properties, class methods, static methods, and Django model fields internally.

### 14. What is monkey patching and when is it dangerous?
Modifying classes/modules at runtime. Dangerous because it can break assumptions, affect global state, cause debugging nightmares, and create maintenance issues.

### 15. How does Python async event loop work internally?
Runs single-threaded with cooperative multitasking. Maintains ready and waiting task queues, executes tasks until they yield control, and processes I/O events using epoll/select.

---

## ⚙️ DJANGO INTERNALS (16-35)

### 16. Explain Django architecture internally.
Follows MVT pattern: Models (database layer), Views (business logic), Templates (presentation). Uses URL dispatcher, middleware chain, ORM, and template engine with request-response cycle.

### 17. How does Django handle request → response cycle?
URL dispatcher → Middleware (request phase) → URL resolution → View execution → Template rendering → Response creation → Middleware (response phase) → Response sent.

### 18. What happens when a Django server starts?
Loading settings → App registry creation → Models loading → App initialization → URL resolution → Middleware building → Template engine loading → Server listening for requests.

### 19. How does Django load settings?
Reads DJANGO_SETTINGS_MODULE environment variable. Imports that module and uses it as configuration source. Allows overriding with environment variables and local settings.

### 20. What is Django app registry?
Internal registry containing all installed applications and their models. Built during startup, accessed via `apps.get_models()` and `apps.get_app_config()`. Essential for ORM operations.

### 21. How do Django signals work internally?
Use observable pattern with Signal class. Receivers are stored in receiver map. When signal sent, all registered receivers are called synchronously. Uses weak references by default.

### 22. Are Django signals synchronous or asynchronous?
Django signals are synchronous by default. They execute immediately in the same thread/process. Async support via async-capable signal handlers (Django 3.1+).

### 23. What are the downsides of signals?
Hard to debug (implicit execution flow), can lead to circular dependencies, performance overhead, signals in migrations can cause issues, and they break the request-response flow transparency.

### 24. How does Django middleware chain work?
Middleware are processed in order defined in MIDDLEWARE setting. Each request goes through process_request methods, then view, then process_response in reverse order.

### 25. What is middleware ordering impact?
Order affects request/response processing. Authentication middleware should be before authorization. Security middleware early. Generally, Django middleware should be before custom ones.

### 26. What is WSGI in depth?
Web Server Gateway Interface - specification defining how web servers communicate with Python web applications. Uses synchronous, callable interface accepting environ and start_response.

### 27. What is ASGI and why was it introduced?
Asynchronous Server Gateway Interface - supports asynchronous communication. Introduced for WebSocket handling, long-lived connections, and better performance under concurrent load.

### 28. Difference between WSGI and ASGI performance?
ASGI handles concurrent connections better with event-loop model. WSGI uses thread/process per request. ASGI better for I/O bound operations and WebSocket connections.

### 29. How does Django ORM connect to DB?
Uses database backend (e.g., django.db.backends.postgresql). Connection created when first needed, stored in thread-local variable. Uses connection pooling via CONN_MAX_AGE setting.

### 30. How does query compilation happen in ORM?
QuerySet → SQLCompiler → Database Compiler → SQL generation with dialect-specific features. Uses AST transformations and parameter binding for safe SQL generation.

### 31. What is QuerySet evaluation delay?
QuerySets are lazy - not executed until iteration, slicing, pickling, or repr() called. Values are cached after first evaluation. All database queries occur at evaluation time.

### 32. What is lazy loading in Django ORM?
Models and QuerySets only load data when accessed. Foreign key fields loaded on first access (causing N+1 issue). Prefetching can load related data eagerly.

### 33. How does Django manage database connections?
Uses connection pool or recreates connections. CONN_MAX_AGE controls connection persistence. Timeout, max connections, and connection closing handled by database backend.

### 34. What is connection pooling?
Pre-creates and reuses database connections to reduce overhead. Django implements via persistent connections with CONN_MAX_AGE > 0. PgBouncer can be used for external pooling.

### 35. What happens during Django migration internally?
Migration file read → State transitions simulation → SQL generation → SQL execution in transaction → Record in django_migrations table. Supports forward/rollback operations.

---

## 🧩 DJANGO ORM MASTERY (36-55)

### 36. What is QuerySet caching and when does it break?
QuerySet caches results after first evaluation. Caching breaks when QuerySet is sliced, evaluated partially, or when database changes between evaluations. Use .all() carefully.

### 37. How does select_related work internally?
Uses SQL JOIN to fetch related objects in same query. Works for ForeignKey and OneToOneField. Results in one large query but prevents N+1 queries for single-level relations.

### 38. How does prefetch_related work internally?
Performs separate queries for each relation and joins in Python. Uses JOIN or IN query for many-to-many and reverse relations. More flexible but uses more memory than select_related.

### 39. When does N+1 problem still occur despite optimization?
When using prefetch_related on nested relations or when you access related objects after filtering. Also occurs when using values() or values_list() with related fields.

### 40. What is defer() and only()?
defer() excludes specific fields from query, only() includes only specific fields. Reduces data transfer by selecting subsets. Works only on model fields, not related objects.

### 41. What is annotate() used for in analytics?
Adds aggregated values to each object in QuerySet. Used for counts, averages, sums per object. Supports complex calculations with F() expressions and functions.

### 42. Difference between ORM aggregation vs SQL aggregation?
ORM aggregation uses QuerySet methods (aggregate(), annotate()). SQL aggregation is at database level. Django ORM translates to SQL aggregates but adds Python-level processing.

### 43. What is F() expression and real use cases?
F() references model field values for database operations. Use cases: increment counters, comparing fields (e.g., price > discount), updating fields without race conditions.

### 44. What is Q() object and complex filtering?
Q() enables complex lookups with OR, AND, NOT conditions. Supports dynamic queries and nested conditions. Essential for advanced search functionality.

### 45. What are subqueries in Django ORM?
Using OuterRef and Subquery to create nested SQL queries. Used for complex filtering based on related data. Example: filtering objects where related count > threshold.

### 46. How do you optimize slow ORM queries?
Use select_related/prefetch_related for related data. Index appropriate fields. Use only()/defer() for large fields. Use values() for dictionaries. Analyze query plans.

### 47. What is query plan (EXPLAIN ANALYZE)?
EXPLAIN ANALYZE shows PostgreSQL query execution plan. Shows indexes used, join methods, estimated vs actual costs. Essential for identifying slow query patterns.

### 48. What is indexing strategy in Django models?
Add db_index=True to frequently filtered fields. Use Meta.indexes for composite indexes. Consider unique_together for uniqueness. Add indexes after analyzing query patterns.

### 49. Composite indexes use cases?
Indexes on multiple columns used together in WHERE clause. Example: (user_id, created_at) for filtering user's posts by date. Also used for covering indexes.

### 50. What is database locking in Django ORM?
Database locking prevents concurrent modifications. Implicit row locking (SELECT FOR UPDATE) and explicit table locking. Use select_for_update() for pessimistic locking.

### 51. What is select_for_update() used for?
Locks selected rows until transaction ends. Used for preventing race conditions when reading then updating. Example: inventory management, ticket booking.

### 52. How do transactions work in Django?
Use transaction.atomic() decorator/context manager. Supports savepoints for nested transactions. Default isolation level depends on database. Can rollback on exceptions.

### 53. What is atomic transaction block?
Wraps database operations in a single transaction. All operations succeed or all fail. Prevents partial updates. Nested atomic blocks create savepoints.

### 54. What is isolation level in DB transactions?
Defines transaction visibility levels: Read Uncommitted, Read Committed (PostgreSQL default), Repeatable Read, Serializable. Affects concurrent transaction behavior.

### 55. How do you prevent race conditions in Django?
Use select_for_update() for pessimistic locking. Use F() expressions for atomic updates. Use transactions with proper isolation. Use Django's built-in database constraints.

---

## 🧱 DATABASE & POSTGRESQL (56-70)

### 56. What is MVCC in PostgreSQL?
Multi-Version Concurrency Control - each transaction sees a snapshot of data at start. Updates create new row versions, enabling high concurrency without read locks.

### 57. How does PostgreSQL handle concurrency?
Uses MVCC with multi-version storage. Readers don't block writers, writers don't block readers. Uses row-level locks for writes. Transaction IDs manage visibility.

### 58. What is vacuum in PostgreSQL?
Garbage collection process that reclaims storage occupied by dead tuples. Prevents transaction ID wraparound. Auto-vacuum runs periodically. Critical for performance.

### 59. What causes slow queries in production?
Missing indexes, outdated statistics, poorly written queries, large joins without proper indexes, query plan changes due to parameterization, and high network latency.

### 60. How do indexes internally work (B-tree)?
B-tree indexes store sorted data in tree structure with logarithmic search. Each node contains key values and pointers. Supports equality and range queries efficiently.

### 61. When indexes hurt performance?
On small tables, high-write tables (overhead), columns with few distinct values, not used in WHERE clauses, and when causing incomplete index scans (too many rows).

### 62. What is normalization vs denormalization in real systems?
Normalization eliminates redundancy (3NF standard). Denormalization adds redundancy for performance (e.g., store computed totals). Used in reporting/analytics systems.

### 63. When would you denormalize in production?
For read-heavy systems, reporting dashboards, caching computed values, high-traffic APIs needing optimized queries. Use materialized views or triggers for maintenance.

### 64. What is deadlock in databases?
Situation where two transactions hold locks needed by each other. PostgreSQL detects and cancels one transaction. Prevent by consistent lock ordering and avoiding long transactions.

### 65. How to detect deadlocks?
Check PostgreSQL logs. Use pg_locks view to see active locks. Monitor for log messages with "deadlock detected". Use logging_deadlock in Django settings.

### 66. What is query execution plan?
Roadmap showing how database executes query: scan methods, join types, filter order, index usage. Available via EXPLAIN. Essential for optimization decisions.

### 67. Difference between clustered and non-clustered index?
Clustered index determines physical row order (Primary Key in PostgreSQL). Non-clustered stores pointers to data rows. PostgreSQL uses heap storage with separate index.

### 68. What is sharding?
Horizontal partitioning across servers based on shard key (e.g., user_id). Improves scalability but complicates queries and transactions. Use for huge datasets.

### 69. What is replication?
Copying data from master to replica servers. Master-slave for read scaling, Master-master for high availability. PostgreSQL supports streaming replication.

### 70. Master-slave vs multi-master architecture?
Master-slave: one write master, multiple read replicas. Simpler but single point of failure. Multi-master: writes to any node, conflict resolution needed. Complex but higher availability.

---

## 🚀 DRF (DJANGO REST FRAMEWORK) (71-82)

### 71. How does DRF serialization pipeline work?
Request data → Serializer validation → create/update → model instance → serialization → JSON/XML response. Includes built-in validation, field mapping, and nested serialization.

### 72. What happens when serializer `.is_valid()` is called?
Runs field validators (required, max_length, etc.). Calls custom validate_<field> methods. Calls validate() method. Populates validated_data. Uses model's validations if ModelSerializer.

### 73. Custom validation flow in DRF?
Field-level: validate_<field_name> method. Object-level: validate() method. Validator functions: pass to validators list. Full error messages returned in serializer.errors.

### 74. How do ViewSets work internally?
Combine related views into single class. Map HTTP verbs to methods (list, create, retrieve, update, destroy). Router generates URL patterns automatically with actions.

### 75. Router vs manual URL mapping?
Router automatically generates URLs with ViewSets. Manual mapping gives more control but requires explicit pattern definition. Router saves time for standard CRUD operations.

### 76. Permission system in DRF architecture?
Uses permission classes chain. Check_* methods determine access. Base classes: IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly. Custom permissions for fine-grained control.

### 77. Authentication flow in DRF?
Request → Authentication class → authenticate() method → user credentials validation → user object returned → set request.user → proceed to permissions check.

### 78. Token vs JWT vs Session authentication?
Token: simple, stored in DB, easy to revoke. JWT: stateless, signed, contains claims, no server storage needed. Session: server-side storage, cookie-based, scalable issues.

### 79. How does pagination work internally?
QuerySet slicing applied after ordering. Settings: page_size, max_page_size. Different classes: PageNumberPagination, LimitOffsetPagination, CursorPagination. Uses SQL LIMIT/OFFSET.

### 80. How do throttling classes work?
Rate limiting based on user IP or user ID. Uses cache for counting (default: Django cache). Anon and user throttling separately. Custom throttling for specific endpoints.

### 81. How do you secure APIs in production?
Use HTTPS, implement rate limiting, JWT with short expiry, input validation, SQL injection prevention (ORM does this), proper CORS settings, and API key rotation.

### 82. How would you version a large API system?
URL versioning: /api/v1/, /api/v2/. Accept header versioning. Query string: ?version=1. Use DRF versioning classes. Maintain backward compatibility between versions.

---

## ⚡ CELERY, REDIS & ASYNC SYSTEMS (83-90)

### 83. How does Celery distribute tasks?
Tasks sent to message broker (Redis/RabbitMQ). Workers consume from queues. Broker holds tasks until workers pick them. Result backend stores task results.

### 84. What happens when a Celery worker crashes?
Task returns to queue (if acknowledged). Replaced tasks retry if configured. Use restart policies (supervisor, systemd). May lose tasks if not durable.

### 85. What is task idempotency?
Task that can be safely retried without side effects. Critical for background jobs. Example: updating user_status instead of incrementing counter. Use unique task IDs.

### 86. How do retries work in Celery?
Counts retries in task context. max_retries and countdown settings. retry() method raises Retry exception. Use exponential backoff for better behavior.

### 87. What is broker vs backend in Celery?
Broker handles task queue (Redis/RabbitMQ). Backend stores results (Redis/DB). Separate configs: BROKER_URL and RESULT_BACKEND. Broker is required; backend optional.

### 88. Redis persistence mechanisms?
RDB (snapshots): periodic saves. AOF (Append-Only File): logs every operation. Both for better safety. Configure via redis.conf or SAVE/AOF parameters.

### 89. When should you NOT use Celery?
For very fast tasks (<50ms overhead), simple operations, when system resource constrained, or when simpler scheduling (cron) suffices. Use Django background tasks for simplicity.

### 90. How do you design background job systems at scale?
Use separate queues for priorities, implement retry mechanisms with backoff, monitor queue depth and worker load, use dead letter queues for failed tasks, and implement circuit breakers.

---

## 🐳 DOCKER & DEVOPS (91-96)

### 91. How does Docker networking work?
Creates isolated network namespaces. Bridge network (default) for containers. Host network for direct access. Overlay networks for multi-host. Uses veth pairs for connectivity.

### 92. Difference between image layers?
Each Dockerfile instruction creates a layer. Layers are cached and reused. Images are read-only. Write operations create copy-on-write layer. Base layers can be shared.

### 93. How does container isolation work?
Uses Linux namespaces (PID, NET, IPC, UTS, MNT) and cgroups. Namespaces provide isolation, cgroups limit resources. Additional security via AppArmor/SELinux.

### 94. What is multi-stage Docker build?
Multiple FROM statements in one Dockerfile. Copy artifacts between stages. Reduces final image size by excluding build dependencies. Example: build in Alpine, final image uses build artifacts.

### 95. How does Nginx act as reverse proxy?
Receives client requests and forwards to backend servers. Handles SSL termination, load balancing, caching, request buffering. Improves performance and security.

### 96. Gunicorn worker types and tuning?
Worker types: sync (default, one request per worker), gevent (async), gthread (threaded). Sync works for most. Tuning: workers = (2*CPUs)+1, timeout settings.

---

## ☁️ AWS & PRODUCTION SYSTEMS (97-100)

### 97. How does EC2 auto scaling work?
Monitors CloudWatch metrics (CPU, memory, custom). Triggered by thresholds. Launch templates define new instances. Scale policies: simple, step, target tracking.

### 98. S3 consistency model explained?
Strong consistency for PUTS/GETS/DELETE since 2020. List operations are eventually consistent. No need for custom consistency handling for most operations now.

### 99. How do load balancers distribute traffic?
Uses algorithms: round-robin, least connections, IP hash (sticky sessions). Layer 4 (ALB) for HTTP/HTTPS, Layer 7 (NLB) for TCP/UDP. Health checks remove unhealthy instances.

### 100. Design a scalable Django system for 1M+ users?
Layered architecture: Load balancers → Web servers (Django) → Caching (Redis) → Database (PostgreSQL master-slave). Use CDN for static files. Workers for async tasks. Auto-scaling for web servers. Read replicas for database reads. S3 for file storage.

---

## 📊 ADDITIONAL QUESTIONS (101-200)

### 🔷 Database Performance (101-110)

**101. What are database connections per second?**
Maximum connections database can handle simultaneously. PostgreSQL default: 100. Monitor pg_stat_activity to track usage. Tune max_connections if needed.

**102. Connection pooling strategies?**
Pgbouncer (external), Django persistent connections (CONN_MAX_AGE), Pgpool-II. Each with different: connection reuse, session pooling, transaction pooling.

**103. Query optimization techniques?**
Use indexes on WHERE/JOIN columns. Avoid SELECT *. Use LIMIT for large datasets. Use EXISTS instead of COUNT for existence checks. Use query plans for analysis.

**104. What is query caching?**
Django QuerySet results are cached within request. Use Memcached/Redis for cross-request caching. Cache querysets, API responses, and expensive calculations.

**105. Database migrations strategies?**
Zero-downtime migrations: Backward-compatible changes first. Add columns null, deploy, then fill data. Rename with django.db.models. Not null changes carefully.

**106. What is database read replica?**
Copy of master database for read operations. Improves read performance and availability. Django can use via database routers. Handles reporting queries.

**107. Write-heavy database optimizations?**
Batch inserts, partition tables, use queues for writes, write to cache then background sync, use TimescaleDB for time-series data, optimize disk I/O.

**108. What is database partitioning?**
Split large tables into smaller pieces by partition key (date, range). Improves query performance and maintenance. PostgreSQL supports range/list/hash partitioning.

**109. Backup strategies?**
pg_dump (logical), pg_basebackup (physical), WAL archiving (point-in-time). Regular automated backups to S3. Test restore procedures regularly.

**110. Disaster recovery plan?**
Multi-region replication. Automated failover. Regular backup testing. RPO (Recovery Point Objective) and RTO (Recovery Time Objective) defined. Document runbooks.

### 🔷 Architecture & Design (111-120)

**111. Microservices vs Monolith?**
Microservices: independent services, separate deployments, technology diversity, complex operations. Monolith: simpler deployment, easier debugging, shared resources, better performance for single app.

**112. When to use microservices?**
Large teams (20+), different scaling requirements, independent release cycles, technology polyglot, organizational alignment. Start with monolith, split when needed.

**113. Service discovery in microservices?**
Consul, Eureka, Kubernetes services. Services register themselves, clients discover via registry. Health checks remove unhealthy instances.

**114. API Gateway patterns?**
Single entry point: routes, auth, rate limiting, caching, logging. Implement with AWS API Gateway, Kong, or custom Django. Centralizes cross-cutting concerns.

**115. Event-driven architecture?**
Services communicate via events (messages). Decoupled, asynchronous, scalable. Uses message brokers (RabbitMQ, Kafka). Useful for notifications, data processing.

**116. CQRS (Command Query Responsibility Segregation)?**
Separate read and write models. Different database schemas. Write model (commands), read model (queries). Complex but improves scalability and flexibility.

**117. Event Sourcing?**
Store state as sequence of events. Rebuild state by replaying events. Audit trail, event replay, temporal queries. Use with CQRS for full pattern.

**118. 12-Factor App methodology?**
Codebase, dependencies, config, backing services, build/release/run, processes, port binding, concurrency, disposability, dev/prod parity, logs, admin processes.

**119. CAP theorem in practice?**
Consistency, Availability, Partition tolerance - choose two. Distributed systems favor AP (eventual consistency) or CP (strong consistency). Trade-offs based on requirements.

**120. Choose architecture decisions?**
Consider: data consistency needs, team expertise, time to market, scalability requirements, operational complexity, budget constraints. Document architecture decisions.

### 🔷 Security (121-130)

**121. OAuth2 and OpenID Connect?**
OAuth2: authorization framework with grants. OpenID Connect: identity layer on OAuth2. Provides tokens (access, refresh, ID token). Used for third-party authentication.

**122. JWT security considerations?**
Short expiry times, use HTTPS, store securely (httpOnly cookies), validate signature, implement refresh tokens, rotate keys, invalidate via blacklist.

**123. CSRF protection in Django?**
Django includes CSRF token middleware. Token in forms and AJAX requests. Validate token on POST, DELETE, PUT. Use SameSite cookies for modern protection.

**124. CORS implementation?**
Cross-Origin Resource Sharing - use django-cors-headers. Configure allowed origins, methods, headers. Essential for API security. Allow specific origins only.

**125. SQL injection prevention?**
Django ORM uses parameterized queries. Never use raw SQL with interpolation. Use .raw() with parameters. Validate user inputs. Use ORM's built-in protections.

**126. XSS protection?**
Django auto-escapes template output. Use safe filter carefully. Validate inputs. Set appropriate headers (Content-Security-Policy). Use HttpOnly cookies.

**127. Rate limiting strategies?**
Per user/IP. Sliding window or fixed window. Implement in Nginx, API gateway, or application level. Use Redis for distributed rate limiting.

**128. Data encryption?**
At rest: database encryption, S3 SSE, encrypted EBS volumes. In transit: TLS/HTTPS. In memory: sensitive data handled carefully. Key management: AWS KMS, HashiCorp Vault.

**129. Audit logging?**
Log user actions: access, modifications, admin operations. Include user ID, timestamp, IP, action. Store securely. Use for compliance and incident investigation.

**130. Security best practices?**
Regular dependency updates, security headers (HSTS, CSP, X-Frame-Options), input validation, output encoding, least privilege principle, regular security audits.

### 🔷 Caching (131-140)

**131. Caching strategies?**
Cache-aside: application manages cache. Read-through: cache loads from DB. Write-through: writes to cache and DB. Write-behind: writes to cache, async to DB.

**132. Cache invalidation patterns?**
TTL (time-based), event-based invalidation, write-through updates. Use cache versioning for schema changes. Clear related caches on updates. Use Redis pub/sub for distributed invalidation.

**133. Django caching backends?**
LocMemCache (local memory), RedisCache (redis), MemcachedCache (memcached), DatabaseCache (DB). Choose based on scale: Redis for production, LocMem for development.

**134. Cache levels?**
Browser cache (static files). CDN cache (assets). Application cache (Django cache). Database cache (query cache). Each level reduces load on next level.

**135. What is cache stampede?**
Thundering herd problem when cache expires. Many requests simultaneously rebuild cache. Prevent with: cache locking, stale-while-revalidate, probabilistic early expiration.

**136. Redis cache patterns?**
Sets for sorting, Hashes for objects, Lists for queues, Sorted Sets for leaderboards, Bitmaps for analytics, Geo for locations. Choose based on use case.

**137. Custom cache keys?**
Include: model name, ID, query parameters. Use version parameter for schema changes. Hash complex parameters. Implement consistent key generation methods.

**138. Cache decorators?**
cache_page for views, cache_control for headers, vary_on_* for different cached versions. Use cache template tag for template fragments. All in Django.

**139. Distributed caching?**
Cache across multiple servers using consistent hashing. Redis Cluster or Memcached servers. Use cache middleware for automatic distribution. Handle cache miss intelligently.

**140. When to avoid caching?**
Real-time data (stock prices), frequently updated data, user-specific data, small datasets. Sometimes database is more efficient. Always invalidate properly.

### 🔷 Testing (141-150)

**141. Django testing structure?**
tests.py with unittest/TestCase classes. Run with python manage.py test. Use fixtures for test data. Database created fresh per test. Isolate tests for reliability.

**142. Unit tests vs integration tests?**
Unit tests: test individual components in isolation, fast, mock dependencies. Integration tests: test components together, test database, slower, catch integration issues.

**143. Mocking in Django tests?**
Use unittest.mock. Mock external services (payment APIs). Mock time for date-dependent logic. Mock signals to prevent side effects. Ensure isolation from real services.

**144. Test database configuration?**
Different DATABASES setting for testing. Use PostgreSQL with template1 for faster creation. Transactional tests rollback changes. Parallel test execution with --parallel.

**145. API testing with DRF?**
APITestCase, APIClient. Test authentication, permissions, serializers, responses. Use reverse for URLs. Test both success and error cases. Test validation thoroughly.

**146. Performance testing?**
Load testing: Locust, JMeter. Endurance testing. Stress testing. Identify bottlenecks before production. Set performance baselines. Monitor during load.

**147. What is TDD?**
Test-Driven Development: write tests first, watch fail, implement code, watch pass, refactor. Improves design and coverage. Can be time-consuming initially.

**148. Test fixtures and factories?**
Fixtures: pre-defined JSON data. Factories: factory_boy for dynamic data. Use for consistent test data. Factory gives more flexibility and is maintainable.

**149. Testing email services?**
Use Django test email backend. Check outbox for sent emails. Test email content, recipients, attachments. Don't send real emails during tests.

**150. CI/CD for Django?**
GitHub Actions/GitLab CI: run tests on each commit, linting, type checking, build Docker image, deploy to staging, run integration tests, deploy to production.

### 🔷 Monitoring & Logging (151-160)

**151. Django logging setup?**
LOGGING dict in settings. Handlers: console, file, sentry. Formatters: simple, detailed. Loggers: django, custom. Levels: DEBUG, INFO, WARNING, ERROR, CRITICAL.

**152. Monitoring tools?**
Prometheus + Grafana for metrics. ELK stack for logs. Sentry for errors. New Relic/Datadog for APM. AWS CloudWatch for AWS resources. Combine for visibility.

**153. Health check endpoints?**
/health for service health. Include: database connection, cache connection, worker status, disk space. Use for load balancer health checks. Return proper status codes.

**154. Application Performance Monitoring?**
APM tools: New Relic, Datadog, Django Silk. Track request times, slow queries, errors, external calls. Identify bottlenecks and optimize. Use in production.

**155. SLIs and SLOs?**
SLIs (Service Level Indicators): response time, error rate, uptime. SLOs (Service Level Objectives): targets for SLIs. Example: 99.9% uptime, <200ms p95 latency.

**156. Distributed tracing?**
Track request across microservices. Tools: Jaeger, Zipkin. Trace IDs propagate between services. Helps debug complex interactions. Essential for microservices.

**157. Error tracking?**
Sentry catches and categorizes errors. Group by issue. Track frequency, affected users. Get notifications. Identify and fix critical issues quickly.

**158. Custom metrics?**
Use Prometheus client, Dogstatsd. Measure: request counts per endpoint, cache hit rates, queue depths, business metrics (orders placed). Alert on anomalies.

**159. Log aggregation?**
Collect logs from all services. Tools: ELK (Elasticsearch, Logstash, Kibana), Loki. Centralized logging for search and analysis. Structured JSON logs for parsing.

**160. Alerting strategies?**
Set up alerts for: error rate spikes, high latency, disk space, service down, certificate expiry. Use PagerDuty/Slack. Avoid alert fatigue - only actionable alerts.

### 🔷 DevOps & Infrastructure (161-170)

**161. Infrastructure as Code?**
Terraform, AWS CloudFormation. Define infrastructure in code. Version controlled. Reproducible environments. Infrastructure changes automated and auditable.

**162. Container orchestration?**
Kubernetes manages containerized apps. Features: auto-scaling, service discovery, rolling updates, self-healing. EKS/AKS/GKE managed versions. Complex but powerful.

**163. CI/CD pipeline stages?**
Source code → Build → Test → Package → Deploy staging → Integration tests → Deploy production. Automated with Jenkins, GitLab CI, GitHub Actions.

**164. Blue-Green deployment?**
Two identical environments. Switch traffic from blue (old) to green (new). Zero downtime. Easy rollback. Requires two environments and database compatibility.

**165. Canary deployments?**
Roll out new version to subset of users. Monitor for errors. Gradually increase percentage. If errors, rollback. Reduces risk. A/B testing compatibility.

**166. Feature flags?**
Toggle features on/off without deployment. Tools: LaunchDarkly, Django waffle. Gradual rollout. Kill switch for problematic features. Essential for continuous delivery.

**167. Zero-downtime migrations?**
Use backward-compatible schema changes. Add new columns before using. Deploy code. Then make nullable/migrate data. Add constraints after data migration.

**168. Service mesh?**
Sidecar proxies for service-to-service communication. Features: traffic management, security, observability. Istio, Linkerd. Adds complexity but control.

**169. Serverless architecture?**
AWS Lambda, Google Cloud Functions. Scale automatically, pay per execution. Good for event-driven workloads. Cold start issues. Not for long-running tasks.

**170. DevOps culture?**
Collaboration between development and operations. Shared responsibility. Automation, monitoring, continuous improvement. Break silos, focus on reliability.

### 🔷 Hard Problems (171-180)

**171. Distributed transactions?**
Two-phase commit for ACID across services. Saga pattern for eventual consistency. Use event-driven compensating transactions. Avoid distributed transactions if possible.

**172. Data consistency across services?**
Eventual consistency with event sourcing. Use event publication with outbox pattern. Idempotent consumers. Reconciliation jobs for correcting inconsistencies.

**173. Handling large file uploads?**
Use direct upload to S3 (presigned URLs). Process in background with Celery. Use multipart upload for large files. Progress tracking. Compress/resize server-side.

**174. Payment processing patterns?**
Idempotent requests (idempotency key). Webhook handling with idempotency. 3D Secure. Payment intents. Handle failures gracefully. PCI compliance required.

**175. Real-time features implementation?**
WebSockets for real-time communication. Django Channels for WebSocket handling. Redis for pub/sub. Handle reconnection, stale connections, authentication.

**176. Search implementation?**
PostgreSQL Full-Text Search for simple needs. Elasticsearch for complex search. Algolia for SaaS. Meilisearch for easy setup. Indexing strategy crucial.

**177. Recommendation systems?**
Collaborative filtering, content-based, matrix factorization. Precompute recommendations. Cache results. Update periodically. Use Redis for fast retrieval.

**178. Data migrations at scale?**
Batch processing (chunked). Use database-specific optimizations (COPY in PostgreSQL). Backup before migration. Validate data integrity. Have rollback plan.

**179. Multi-tenancy patterns?**
Separate databases (highest isolation). Separate schemas (PostgreSQL). Shared schema with tenant_id. Each has trade-offs: complexity, scalability, isolation.

**180. Legacy system migration?**
Strangler pattern: gradually replace functionality. Proxy between old and new. Migration scripts for data. Parallel running. Rollback plan. User communication.

### 🔷 Interview Specific (181-190)

**181. "Why Django over other frameworks?"**
Batteries-included philosophy, excellent ORM, built-in admin, security features, scalability, large ecosystem, Python integration, strong community, battle-tested.

**182. "Explain a challenging bug you solved."**
Production query performance issue. Identified N+1 queries with Django Debug Toolbar. Used select_related and query optimization. Reduced response time from 5s to 200ms.

**183. "How do you handle API versioning?"**
Use URL versioning (/api/v1/). Maintain backward compatibility for minor changes. Create new version for breaking changes. Deprecation policy for old versions.

**184. "Explain your Django development setup."**
Virtual environment, Postgres locally, Redis for caching, Docker for dependencies, pre-commit hooks (black, flake8), pytest for testing, environment variables.

**185. "How do you ensure code quality?"**
Pull request reviews. Automated linting and tests in CI. Code coverage tracking. Type hints (mypy). Documentation. Code quality standards (PEP8). Regular refactoring.

**186. "What is your deployment process?"**
CI pipeline runs tests → Builds Docker image → Pushes to registry → Deployment to staging → Integration tests → Blue-Green deployment to production. Monitored with Sentry.

**187. "How do you handle production incidents?"**
Alert triggers → Acknowledge → Investigate logs/metrics → Identify cause → Apply fix → Validate → Document post-mortem → Prevent recurrence with improvements.

**188. "What is your experience with team collaboration?"**
Technical discussions in design docs. Pair programming for complex tasks. Clear PR descriptions. Documentation updates. Regular sync meetings. Mentoring junior developers.

**189. "Describe a project you're proud of."**
E-commerce API handling 100k orders/day. Used Django + DRF. Optimized with caching, Celery for async tasks, read replicas. Reduced costs 40% with better architecture.

**190. "What do you look for in a team?"**
Strong engineering culture, learning opportunities, code reviews, documentation practices, work-life balance, impactful work, good mentorship, tech innovation.

### 🔷 System Design (191-200)

**191. Design URL shortener system.**
URL → hash (base62) → store mapping (Redis cache + DB). Statistics tracking. Use distributed ID generator. Scale: sharding by short_code. Pre-generate IDs.

**192. Design chat application.**
WebSockets for real-time. Store messages in database. Redis for pub/sub between servers. Handle offline messages. Read receipts. Chat history pagination. Push notifications.

**193. Design social media feed.**
Timeline: pre-compute aggregated feed. Write to feed cache on post creation. Push model for small followers. Pull model for large followers. Rank content algorithmically.

**194. Design notification system.**
Events → Notification queue → Processors for different channels (email, push, SMS). Templates, delivery preferences. Real-time and batch modes. Rate limiting.

**195. Design file storage system.**
Content-addressable storage (hash-based). Chunk upload for large files. Metadata in database. CDN distribution. Compression, resizing, transformation. Access control.

**196. Design rate limiter.**
Sliding window algorithm (Redis sorted sets). Token bucket for bursts. Distributed with Redis. Per endpoint/user/IP. Separate limits. Handle gracefully.

**197. Design recommendation system.**
Offline batch computation of recommendations. Store results (Redis/DB). Rank and filter in real-time. A/B test algorithms. Personalization based on user behavior.

**198. Design log aggregation system.**
Log shipper → Buffer (Kafka) → Processor (Elasticsearch) → Storage → Search/Visualize. Real-time and offline analysis. Retention policies. Alerting on patterns.

**199. Design leaderboard system.**
Redis sorted sets for real-time scores. Update on score changes. Get top K efficiently. Periodic database backups. Handle high write and read concurrency.

**200. Design full-text search system.**
Indexing pipeline (document → tokenization → index). Query parsing and scoring. Elasticsearch for distributed search. Autocomplete with prefix queries. Relevance tuning.

---

## 📝 KEY MEMORY TRIGGERS

### Before Interview Quick Review:
1. **Django Lifecycle**: URL → Middleware → View → ORM → Template → Response
2. **Optimization**: select_related for FK, prefetch_related for M2M, index wisely
3. **N+1**: Use prefetch_related/select_related to avoid
4. **DB**: MVCC, indexes, EXPLAIN ANALYZE
5. **Caching**: Redis for performance, invalidate on updates
6. **Security**: JWT, CORS, CSRF, SQL injection (ORM handles)
7. **System Design**: Scale horizontally, cache, async, read replicas


---

**💡 Pro Tip**: For any question, provide: Definition → Use case → Example from your experience.

**Good luck! 🎯**

