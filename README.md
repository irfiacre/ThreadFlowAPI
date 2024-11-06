# ThreadFlowAPI
This is a forum API built using Django REST Framework, designed to facilitate dynamic and community-driven conversations. It offers a complete backend solution for managing discussions, user interactions, and content moderation across various categories, making it ideal for building modern forums and discussion platforms.


## Features:

| Feature                               | Description                                                      | Completed |
|---------------------------------------|------------------------------------------------------------------|-----------|
| **1. User Authentication**            |                                                                  |           |
| Register & Login                      | Users can register and log in to the forum.                      | [/]       |
| JWT Authentication                    | Use JSON Web Tokens (JWT) to manage authentication.              | [/]       |
| User Profiles                         | Each user has a profile                                          | [/]       |
| Roles and Permissions                 | Admin, Moderator, and User roles with specific permissions.      | [/]       |
| **2. Thread Management**              |                                                                  |           |
| Create a Thread                       | Users can create new discussion threads within a specific category. | [/]       |
| Edit/Delete a Thread                  | Users can edit or delete their own threads.                      | [/]       |
| Thread Categories                     | Organize threads into categories (e.g., Technology, Sports).     | [/]       |
| Tagging                               | Users can add tags to threads for better organization.           | [-]       |
| Thread Locking                        | Admins or moderators can lock threads to prevent further replies. | [-]       |
| **3. Post Management**                |                                                                  |           |
| Reply to a Thread                     | Users can post replies within threads.                           | [/]       |
| Edit/Delete a Reply                   | Users can edit or delete their own replies.                     | [/]       |
| Thread Pagination                     | Paginate long threads for easier viewing.                       | [ ]       |
| Quote a Reply                         | Users can quote other users' replies when responding.           | [ ]       |
| Markdown Support                       | Allow users to format replies using Markdown (or basic HTML).    | [ ]       |
| Upvoting/Downvoting                   | Users can upvote or downvote replies to indicate helpfulness.    | [ ]       |
| **4. Moderation Tools**               |                                                                  |           |
| Flag Inappropriate Content            | Users can flag threads or replies for review by moderators.      | [ ]       |
| Ban Users                             | Admins can ban users for inappropriate behavior.                 | [ ]       |
| Content Moderation                    | Admins and moderators can delete or edit inappropriate content.  | [ ]       |
| View Reports                          | Moderators can view flagged content reports.                     | [ ]       |
| **5. Notifications System**           |                                                                  |           |
| Thread Updates                        | Users get notified when someone replies to their thread.         | [ ]       |
| Mention Notifications                 | Users are notified if someone mentions them using @username.     | [ ]       |
| Subscription to Threads               | Users can subscribe to threads to get notifications for new replies. | [ ]     |
| **6. Search & Filter**                |                                                                  |           |
| Search by Thread Title or Content     | Users can search for specific threads or posts.                 | [ ]       |
| Search by Category or Tags            | Filter threads by category or specific tags.                    | [ ]       |
| Sort Threads by Date, Popularity     | Allow sorting based on different criteria (e.g., latest, most upvoted). | [ ]   |
| **7. Thread Analytics**               |                                                                  |           |
| View Counts                           | Track how many views each thread has.                           | [ ]       |
| Reply Count                           | Display the number of replies each thread has received.          | [ ]       |
| Most Popular Threads                  | Show popular threads based on views and replies.                 | [ ]       |
| **8. User Reputation System**         |                                                                  |           |
| Points System                         | Users gain points for starting threads, getting upvotes, and replying to posts. | [ ] |
| Rank Levels                           | Users unlock rank levels (e.g., Newbie, Expert) based on points. | [ ]     |
| Badges & Achievements                 | Award badges for specific achievements (e.g., "100 replies posted"). | [ ]   |
| **9. Admin Dashboard**                |                                                                  |           |
| User Management                       | Admins can manage users (view/edit/delete).                     | [ ]       |
| Category Management                   | Admins can create, edit, or delete forum categories.            | [ ]       |
| View Reports                          | Display user activity reports, flagged content, and usage statistics. | [ ]   |
| **10. Additional Features**           |                                                                  |           |
| Thread Pinning                        | Admins or moderators can pin important threads to the top of the category. | [ ]  |
| Private Messaging                     | Allow users to send direct messages to each other.               | [ ]       |
| Anonymous Posting                     | Option for users to post replies anonymously (with moderation control). | [ ] |
| Thread Polls                          | Users can create polls in threads and see poll results.         | [ ]       |
| **Bonus**                             |                                                                  |           |
| Rate-Limiting                         | Prevent spamming by limiting the number of posts a user can make. | [ ]    |
| Content Caching                       | Cache popular threads to improve performance.                    | [ ]       |
| API Documentation                     | Use tools like Swagger or Postman to document the API.          | [ ]       |

