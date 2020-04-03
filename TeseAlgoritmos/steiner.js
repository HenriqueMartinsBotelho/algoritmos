vertices = [];
edges = [];

function setup() {
    createCanvas(600, 600);
    
    // Random points 
    for (var i = 0; i < 3; i++) {
        var v = createVector(random(width), random(height));
        vertices.push(v);
    } 
}


class Graph { 
    constructor() { 
    this.numberOfNodes = 0;
    this.adjacentList = {
    }; 
  } 
  addVertex(node)  { 
    this.adjacentList[node]=[];
    this.numberOfNodes++;
   } 
   addEdge(node1, node2) { 
    // this.adjacentList[node1]=[]; <------------ Remove this line
     this.adjacentList[node1].push(node2);
     this.adjacentList[node2].push(node1); // <-- Add this line
   }
  
  showConnections() { 
    const allNodes = Object.keys(this.adjacentList); 
    for (let node of allNodes) { 
       let nodeConnections = this.adjacentList[node]; 
       let connections = ""; 
       let vertex;
    for (vertex of nodeConnections) {
        connections += vertex + " ";
      } 
       console.log(node + "-->" + connections); 
      } 
     } 
    } 


/*function mousePressed(){
    var v = createVector(mouseX, mouseY);
    vertices.push(v)
}*/

function draw() {
    background(100);

    // PRIM

    var reached = [];
    var unreached = [];

    for (let i = 0; i < vertices.length; i++) {
        unreached.push(vertices[i]);
    }

    reached.push(unreached[0]);
    unreached.splice(0, 1);
    
    while(unreached.length > 0){
        var record = 100000;
        var reachedIndex;
        var unreachedIndex;
        for (var i = 0; i < reached.length; i++) {
            for (let j = 0; j < unreached.length; j++) {
                var v1 = reached[i];
                var v2 = unreached[j];
                var distance = dist(v1.x, v1.y, v2.x, v1.y);
                if(distance < record){
                    record = distance;
                    reachedIndex = i;
                    unreachedIndex = j;
                    var edge = [i, j];
                }
            }
        }
        stroke(255);
        line(reached[reachedIndex].x, reached[reachedIndex].y, unreached[unreachedIndex].x, unreached[unreachedIndex].y);
        edges.push(edge);
        console.log(edge);
        reached.push(unreached[unreachedIndex]);
        unreached.splice(unreachedIndex, 1);
    }

    // Criando grafo com base nas arestas da árvore de Prim

    var g = new Graph();
           
    // adding vertices 
    //for (var i = 0; i < vertices.length; i++) { 
     //   g.addVertex(i); 
    //} 

    g.addVertex('0');
    g.addVertex('1');
    g.addVertex('2');

    for (var i = 0; i < edges.length; i++) {
        g.addEdge(edges[i][0], edges[i][1]);
    } 

    console.log(edges);

    //Adj = g.getAdj();

    g.showConnections();

     //for (let [key, value] of Adj) {
    //    console.log(key + " " + value);
        //  document.write("<br>");
    //}
     

    
    

    fill(255);
    stroke(255); // Change the color
    for (var i = 0; i < vertices.length; i++) {
        ellipse(vertices[i].x, vertices[i].y, 10, 10);
    }
    noLoop();
}
  
  

