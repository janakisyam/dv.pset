function setup()
{
  createCanvas(800,800);
  strokeWeight(2);
  noFill();
}
var w=100,h=100,x=0;
function draw()
{
    translate(0,200);
    y=50*sin(x*PI/16);
    x=x+1;
    point(10*x,y);


}
