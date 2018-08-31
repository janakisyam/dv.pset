function setup()
{
  createCanvas(600,400);
  noFill();
  strokeWeight(2);
}
var x=1, speed=5;

function draw()
{
    //translate(0,200);
    clear();

   ellipse(x,200,100,100);
   ellipse(600-x,200,100,100);
   x = x + speed;
   if(x>600)
   {
     speed = speed - 1;
   }
   else if (x<1)
   {
     speed = speed + 1;
   }
}
