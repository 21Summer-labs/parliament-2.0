# Parliament 2.0

## Abstract
The government of Kenya has shown inefficiency in listening to its citizens. The representatives elected by the people are failing to fulfill their mandate effectively. We propose a Blockchain-based solution featuring voting, discussions, a native cryptocurrency, and a community platform to enhance citizen engagement and governmental transparency. This system will leverage artificial intelligence to moderate and guide users, ensuring a seamless and informed interaction with the platform.

## Introduction

### Problem Statement
The Kenyan government has consistently failed to effectively listen to and represent its citizens. Elected representatives are not adequately fulfilling their role of reflecting the will of the people in governmental decisions and policies.

### Solution
We propose the development of "Parliament 2.0," a blockchain-based platform designed to facilitate transparent and secure voting, enable discussion on bills, support a native cryptocurrency, and foster a community where citizens can engage with each other and the government. Artificial intelligence will serve as a moderator and guide, helping users navigate the system and understand its functionalities.

### Objectives
- Develop a blockchain-based application.
- Enable developers to contribute easily to the system.
- Empower citizens to participate and host the system.
- Create a rewarding mechanism within the system.
- Facilitate interaction and engagement among users and within the system.

## Methodology

### User Interaction
Users will log into the system using social accounts (Google, X, or Facebook). Once logged in, users can:
- Engage in community discussions.
- Vote on featured bills.
- Make posts or support causes.
- Earn native currency by participating in system activities.

### Bill Creation
Bills are created from discussions within the community. Documents such as the constitution can be stored on the blockchain. The system is built around transparency and trust, with every transaction being visible on the blockchain, ensuring everyone has access to the latest information.

### AI Integration
An AI system will assist users by explaining system functionalities and aiding potential developers. The blockchain will be transparent, with every transaction recorded and accessible to users. The system emphasizes transparency and trust.

## Use Cases
- Voting on bills and causes.
- Storing important documents.
- Transferring money within the system.

## Functional Requirements
- E-wallet for transactions.
- Native cryptocurrency.
- Ethereum-based blockchain.
- Smart contract system.
- Document management system.
- Retrieval-Augmented Generation (RAG) for AI to find context.
- Accessible mobile and web applications.
- AI voice assistant for user support.

## Nonfunctional Requirements
- High availability.
- Modifiability for continuous improvement.
- Interoperability with social accounts and wallets.
- Testability for reliability.
- Security to protect user data and transactions.
- Performance to handle high traffic.
- Usability for a seamless user experience.

## Data Model
- User
- Vote
- Bill
- Cause
- Post
- Comment
- Discussion
- Tokens
- Community

## UI Model

### Pages
- **Home Page**: Displays latest posts, top discussions, and top polls.
- **Bills**: List of bills available for voting.
- **Causes**: Causes that users can support, such as environmental initiatives.
- **Discussions**: Ongoing discussions that users can join.
- **Communities**: Lists of various communities (e.g., counties, sub-counties, wards, constituencies).
- **Chat with AI**: Direct messaging with the AI assistant.
- **Profile Page**: User stats, karma, and blockchain views.

### Components
- **Top Navbar**: Displays the number of tokens earned, direct message icon, hamburger menu, and settings.
- **Bottom Navbar**: Navigation to home, discussions, chat with AI, explore communities, and profile.

## Architecture

### System Interfaces
- **LLM APIs**: For AI functionalities.
- **3rd Party OAuth Providers**: For social login (Google, X, Facebook).
- **MetaMask**: For blockchain interactions.

### Client-Server Architecture
- **Client**: Based on Flutter for cross-platform compatibility.
- **Server**: Comprises a dedicated node server for processing transactions and updating the blockchain, and a Firebase server for real-time updates and data management.

### MVC Pattern
- The system will implement a Model-View-Controller pattern to ensure separation of concerns and ease of maintenance.

### Decentralized Technology
- The choice between a shared data source will be discussed further to determine the most efficient and secure implementation.

By leveraging blockchain technology and integrating AI, Parliament 2.0 aims to create a transparent, secure, and engaging platform for Kenyan citizens to participate in their governance actively.
