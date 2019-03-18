
PIXI.utils.sayHello();
var app = new PIXI.Application(700 , 700, {transparent : true});
document.getElementById("display").appendChild(app.view);
//var container = new PIXI.Container();

console.log("hellow universe ");
var water = PIXI.Sprite.fromImage("water1.png");
var dial = PIXI.Sprite.fromImage("dial1.png");
var meter = PIXI.Sprite.fromImage("meter1.png");

water.y = app.screen.height  / 2;
water.x = (app.screen.width /2) - 155;

dial.y = app.screen.height  / 2 + 70;
dial.x = app.screen.width /2 - 40;

meter.y = app.screen.height  / 2 -210;
meter.x = app.screen.width /2  - 245;

dial.pivot.x += 20;
dial.pivot.y = (app.screen.height /2) -150;
//container.addChild(dial);
//container.pivot.x = container.width/2;  
//container.pivot.y = container.height/2;

//water.blendMode = new PIXI.BLEND_MODES.COLOR;
app.stage.addChild(water);
app.stage.addChild(dial);
app.stage.addChild(meter);
dial.rotation =  -120.2;
var right = true;
app.ticker.add(function(delta){
    var a = document.getElementById("amount").value;
    //water.rotation += 0.1*delta;
    if(a != 's'){
        if( right){
            dial.rotation += 0.07 * delta;
            if(dial.rotation>-118){
                right = false;
                console.log("false");
            }
        }
        else {
            dial.rotation -= 0.07 * delta;
            if(dial.rotation < -121){
                right = true;
                console.log("true");
            }
        }
    }
})

// -30