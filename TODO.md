# TODO

**Make sure to keep each stage as simple as possible - views should start off rough, prioritising functionality over
asthetics. All polish can be done when a final product/mvp is implemented**

- [ ] Design / mock data structures and models required for an MVP
    - Also, how will this be reflected in the code. Different between db schema models and api request and response
      models etc...
- [ ] Decide on a database (document makes sense -> maybe mongo etc...)
    - This relates to models/data structures as will have to think about schemas etc...
- [ ] Build services for controller methods.
    - This will mainly be connecting api endpoints to database data
- [ ] Once endpoints for creating a user, creating a project, and creating a discussion within a project are done - can
  start thining about creating basic Views
    - In the future - need to decide on a front end framework to use dedicated.
    - Should this be mobile compatible from the start? or would it make more sense to start with a lightweight web
      framework such as svelte etc...
- [ ] After basic views are implemented, consider other interactions that aren't specific to a single discussion
    - Project searching (tags, domains, etc...)
    - User to user interactions (replies, followings? etc...)
    - More complex project structures (main megathread/landing discussion page, canvas/whiteboard for the project,
      etc...)
    - All of these will require data structure modifications and serious front end views creations
