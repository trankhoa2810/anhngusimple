const config = {
    app: {
        port: process.env.PORT || 8080
    },
    db: {
        url: "mongodb+srv://mongo:PAl6jCH2OSC3kwb2@cluster0.4ez1y.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        // url: "mongodb://localhost:27017/anhngusimple"
    },
    jwt: {
        secret: "anhngusimple-secret-key"
    }
};

module.exports = config;
