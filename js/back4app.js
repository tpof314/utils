
import Parse from 'parse'

Parse.serverURL = 'https://mygame-tpof314.back4app.io'
Parse.initialize(
  '<APP-ID>', // This is your Application ID
  '<KEY1>', // This is your Javascript key
  '<KEY2>'  // This is your Master key (never use it in the frontend)
);

class Game {
    constructor() {
        this.client = new Parse.LiveQueryClient({
            applicationId: '<APP-ID>', // This is your Application ID
            javascriptKey: '<KEY1>', // This is your Javascript key
            serverURL: "wss://<SOMETHING>.back4app.io"
        });
        this.client.open();
        this.GData = Parse.Object.extend('game');
        this.gameObject = {};
    }
    
    bindGameObject(objId, defaultObj) {
        var query = new Parse.Query(this.GData);
        query.equalTo("oid", objId);
        query.find().then((results) => {
            if (results.length > 0) {
                this.gameObject = results[0];
                this.objId = objId;
                console.log('Game Object Found: ', this.gameObject);
            }
            else {
                this.gameObject = defaultObj;
                this.objId = objId;
                this.createGameObject(objId, defaultObj);
                console.log("Game Object Not Found, Create a new one. ", this.gameObject);
                alert("Game object NOT found. A new one is created. " + 
                "Refresh the window to load the game again.");
            }
        }, (error) => {
            console.log(error);
        })
    }

    createGameObject(objId, defaultObj) {
        var myNewObject = new this.GData();
        myNewObject.set("oid", objId);
        myNewObject.set("data", defaultObj);
        myNewObject.save().then(
          (result) => {
            console.log('game created', result);
          },
          (error) => {
            console.error('Error while creating game: ', error);
          }
        );
    }

    updateObject(gameObj) {
        this.gameObject.set("data", gameObj);
        this.gameObject.save().then((response) => {
            console.log('Updated game', response);
          }, (error) => {
            console.error('Error while updating game', error);
        });
    }
}

var game = new Game()
export default game;

