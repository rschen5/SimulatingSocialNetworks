# SimulatingSocialNetworks


A simple model for replicating user behavior in online social networks.

![image](https://media.github.ncsu.edu/user/22068/files/aea403e2-4701-403a-a3ea-e23869d0410f)


[Mesa Library](https://mesa.readthedocs.io/en/stable/) to run our simulations. Our model includes various agents representing users, who interact with each other through creating, viewing, or liking posts. Users are placed in smaller networks within the overall social network and can interact with other users in the same smaller network. Users can leave and join new networks, and both users and posts can have beliefs, emotions, and sentiments that are affected by other users or posts over time.

## Model Implementation:

**Agents:**

Agents can be real people (Users) or bots. Possible actions are as follows:

1. Create a new post (Users only): Based on the personality of the user, users can create a post in their network visible to all other users in the network.
2. Duplicate a post (Bots): When a bot sees a post that they like, they duplicate the post in the network
3. View a post (Users only): Users can view a certain amount of posts based on the time they spend on the social network. This time is determined randomly when users are created, different users spend different amounts of time in the network. Users view posts that are sorted based on the time created or their popularity. They can become dissatisfied with the network over time based on posts they see.
4. Like a post (Both users and bots): Agents can like posts based on their beliefs and how they feel
5. Report fake posts (Users only): Users can report posts they think are fake.
6. Update Beliefs and Emotions (Users Only): Users' beliefs get updated when they see a post. And based on their personality and post, they feel good or bad.
7. Move to other networks (Users only): Users when they are unsatisfied with a network, they can randomly decide to move to other networks

Agents have the following attributes:

1. Agreeableness: [real number 0 to 1] High agreeableness means more cooperative, helpful, and interpersonally successful. Highly agreeable people tend not to bad mouth [1]. Thus, we used this factor to reduce the number of negative posts users create.
2. Extraversion: [real number 0 to 1] High extraversion means more likely to express or share. High extraversion means users process the information more positively and thus are less impacted by negative posts. [2]
3. Neuroticism: [real number 0 to 1] Neuroticism refers to emotional instability, and people high in neuroticism tend to have mood swings and emotional anxiety. High neuroticism means users are more impacted by negative news and tend to create more negative posts. [2]
4. Emotions: [real number -1 to 1] -1 refers to extreme negative emotions, and 1 refers to positive emotions. The emotions determine the sentiment of the posts the user creates.
5. Category: [nominal variables 1 to 5] It refers to the category the agent belongs to. For example, a category of 1 may refer to the agent's profession in a tech-related field. This category impacts how much users' emotions change when they see posts related to their field. [3]
6. Beliefs: [real number 1 to 5] Belief refers to the side of the spectrum a user is in for a category. For example, if the category is politics, 1 means conservative, 3 means neutral, and 5 means liberal.
7. Level of activity
  1. Tendency to create a post: [positive real number] The attribute that determines how often a user creates a post in each step (unit of time)
  2. Time spent per unit visit: [positive integer] The attribute that determines how much time a user spends, which determines how many posts they see each step.
8. Exploration: [real number 0 to 1] It determines how likely a user is to move to other networks.
9. Exposure to false news: [real number 0 to 1] Determines how much false information a user has, which determines the amount of false information in the post they create.
10. Other variables: There are other variables such as is\_bot, posts\_seen, posts\_liked, networks\_visisted, is\_removed, number\_of\_content\_removed, and number\_of\_fake\_reported that are used to track user status.

**Posts:**

Posts are news, ideas, or opinions that agents create or share in a subnetwork. Only users in the same network can interact with the post. Posts have beliefs (derived from the post creator's beliefs), a falseness factor (percentage of false information), a novelty factor (how novel is the post's information), and a sentiment score, among other factors. Posts are accessed by users from a global dictionary which links the network with the respective list of posts.There are three types of these global post dictionaries:

1. NEW\_POSTS: This contains all the new posts created by agents in each step. The posts are shuffled once all new posts are created.
2. TOP\_POSTS: This contains the most liked posts throughout the history of the social network in each community.
3. HOT\_POSTS: These keep the upcoming or rising posts in the community by factoring in how new they are and how many views/likes they got recently.

Posts have the following attributes:

1. Proportion of False information in the post: [real number 0 to 1] It represents how much false information a post contains relative to truth.
2. Beliefs and Category: These are similar to the Agent's beliefs and Category. When agents create posts, they impart some of their beliefs into the post.
3. Novelty: [real number 0 to 1] It represents the amount of new information contained in the post. If a user has already seen the post or the parent post, then this value reduces to 0 for that user
4. Sentiment: [real number 1 to 5] It represents how positive or negative the post is.
5. The number of times reported fake: [positive integer] It represents the number of times the post was reported fake by users. It is used to moderate communities and ban users.
6. Other variables: We keep track of a number of other variables such as author, post\_parent, number\_of\_likes, users\_who\_liked, users\_who\_viewed, hotness\_score, top\_score, and timestamp as well.

**Network/Community:**

A network is a community formed by a group of agents where agents interact with each other through posts. Each network has its own policy to moderate the posts posted. Each network is dedicated to some category and has certain beliefs leaning toward that category (positive or negative). They can remove posts as well as agents based on their policy.

Most properties of network properties are handled by a global variable that has two specific properties:

1. Controversy Score: [probability] This determines how likely the post with opposing views is to be deleted from the network. We have three different categories: High (0.9), Medium(0.5), and Low(0.1)
2. Irrelevant Score: [probability] This determines how likely a post that is irrelevant to the community will be removed. We have two categories for this: High (0.9) and Low(0.1)

We also track the average belief of all the posts currently in the network.

**Social Network:**

Social Network is the whole structure that contains all agents, networks, and posts. It will start with some number of networks with some random number of agents in them. Each social network contains a grid of cells, each cell representing a different network or community. Agents or users move to different grid cells to join different networks within the Social Network.

In our implementation, the model class represents the whole network and the parameters we pass to the network determine how long we run the system and different attributes for agents and sub\_networks.


**Files:**
* model.ipynb: Network model
