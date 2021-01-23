
var colours = ["red", "blue", "green", "yellow"];
var gamePattern = [];
var userClickedPattern = [];
var level=0;

$( document).on("keypress",function(){nextSequence();
});

function nextSequence() {

  var rand = Math.floor(Math.random() * 4);
  var chosen = colours[rand];
  gamePattern.push(chosen);


  $("#" +chosen).fadeIn(100).fadeOut(100).fadeIn(100);
level+=1;
$("h1").html("LEVEL"+level);

}

$(".btn").click(function() {
var userChosenColour = $(this).attr("id");
userClickedPattern.push(userChosenColour);
press($(this));
checkans((userClickedPattern.length)-1);

});

function press(cur){

  cur.addClass("pressed");
setTimeout(function(){cur.removeClass("pressed");},200);

}

function checkans(cl){
if(userClickedPattern[cl]===gamePattern[cl]){



  if (userClickedPattern.length === gamePattern.length){

userClickedPattern=[];
    setTimeout(function () {
      nextSequence();
    }, 1000);

  }

}
 else {
    gamePattern = [];
    userClickedPattern = [];
   level=0;

  $("body").addClass("game-over");
  setTimeout(function(){
      $("body").removeClass("game-over");
  },2000)

  $("h1").html("Game Over, press any key to Restart");



}
}
