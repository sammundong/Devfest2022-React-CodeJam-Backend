CREATE TABLE productinfo (
    id INT NOT NULL,
    userID INT NOT NULL,
    name VARCHAR(30) NOT NULL,
    img VARCHAR(200) NOT NULL,           
    price FLOAT NOT NULL,          
    dates DATE, /*'YYYY-MM-DD'*/
    category VARCHAR(30) NOT NULL,
    info VARCHAR(500) NOT NULL,
    chats INT NOT NULL,
    favorites INT NOT NULL,
    views INT NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE userinfo (
    userID INT NOT NULL,
    profileImg VARCHAR(200) NOT NULL,
    userName VARCHAR(30) NOT NULL,
    location VARCHAR(30) NOT NULL,
    rating FLOAT NOT NULL,
    PRIMARY KEY (userID)
);