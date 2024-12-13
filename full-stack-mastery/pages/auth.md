
Authentication vs authorization

Authentication and authorization are two distinct processes used in security:

- **Authentication**: This process verifies the identity of a user or service. It's about confirming that someone is who they claim to be. Common methods include passwords, biometrics, and security tokens.

- **Authorization**: This process determines what an authenticated user or service is allowed to do. It's about granting permissions to access resources or perform actions. Authorization typically involves roles and permissions.

In summary, authentication is about verifying identity, while authorization is about granting access rights.

There are several ways to perform authentication:

* Password-based Authentication: Users provide a username and password to verify their identity.

* Multi-Factor Authentication (MFA): Combines two or more independent credentials (e.g., password and a security token).

* OAuth: A token-based authentication framework that allows applications to access resources on behalf of a user.

* JWT (JSON Web Tokens): A compact, URL-safe means of representing claims to be transferred between two parties.

* SSO (Single Sign-On): Allows users to authenticate once and gain access to multiple systems without re-entering credentials.

* Biometric Authentication: Uses unique biological traits (e.g., fingerprints, facial recognition) to verify identity.

* SSH Keys: Uses cryptographic keys for authenticating users and machines in SSH protocol.

Each method has its own use cases and security implications.

Authorization can be implemented in various ways depending on the requirements of your application. Here are some common methods:

Role-Based Access Control (RBAC): Define roles within your application, each with specific permissions, and assign these roles to users.

Attribute-Based Access Control (ABAC): Use attributes (e.g., user, resource, environment) to define and enforce access policies.

Access Control Lists (ACLs): Maintain a list of permissions attached to objects specifying which users or system processes can access objects.

OAuth Scopes: Use OAuth scopes to define the level of access granted to third-party applications.

Policy-Based Access Control (PBAC): Create and manage policies that define the rules for access control.

These methods can be used individually or in combination to enforce fine-grained access control in your application.



The OAS REST API exposes functionality for reading and writing real-time and historical Tag Data, Trend Data, and Alarms. Additionally, the API can be used for managing OAS Server configurations. All operations require an authenticated session.
