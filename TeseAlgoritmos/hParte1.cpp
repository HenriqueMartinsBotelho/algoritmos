read
quiet on;
replace_load "st.fe";
background:=WHITE;
define v1 real[2];
define v2 real[2];
im:=max(vertices,id);
ct:=0;dt:=0;cd:=1;
el:=sum(edges,length);
ck:=clock;wl:=0;
quiet off;print ck;quiet on;
foreach edge ee do  
  wl := wl + (ee.vertex[1].vw+ee.vertex[2].vw)*ee.length;

function integer fid(integer fn,integer sn,integer tn){
  if (fn=sn) then return tn else return sn;
 };

sc:={
foreach vertex vv where valence>1 do{
  mc:=-1/2;ff:=1;sf:=2;
  if dt then 
    cd:=(vv.id<=im)&&(max(vv.edges,color)<2);
  if cd then{
   for (fnx:=1;fnx<=valence-1;fnx++)
    for (snx:=fnx+1;snx<=valence;snx++){
      v1[1]:=vv.edge[fnx].x;v1[2]:=vv.edge[fnx].y;
      v2[1]:=vv.edge[snx].x;v2[2]:=vv.edge[snx].y;
      ca:=(v1[1]*v2[1]+v1[2]*v2[2])/sqrt(v1[1]^2+v1[2]^2)/sqrt(v2[1]^2+v2[2]^2);
      if ca > mc then
        {mc:=ca;ff:=fnx;sf:=snx;};
    };
  };
  if !dt then{
    ce:=vv.edge[ff].length;
    be:=vv.edge[sf].length;
    ae:=sqrt(be^2+ce^2-2*mc*be*ce);
    if (ce^2>=ae^2+be^2+ae*be)||(be^2>=ae^2+ce^2+ae*ce) then{
      id1:=fid(vv.id,vv.edge[ff].vertex[1].id,vv.edge[ff].vertex[2].id);
      id2:=fid(vv.id,vv.edge[sf].vertex[1].id,vv.edge[sf].vertex[2].id);
      mw:=minimum(vv.vw,minimum(vertex[id1].vw,vertex[id2].vw));
      if ce > be then{
        vertex[id2].vw:=mw;
        vv.edge[ff].color:=RED;
        vv.edge[sf].color:=MAGENTA;
      }
      else{
        vertex[id1].vw:=mw;
        vv.edge[ff].color:=MAGENTA;
        vv.edge[sf].color:=RED;
      };
      ne:=new_edge(id1,id2);
      edge[ne].color:=BLUE;
      dissolve edges where color=RED;
      ct:=ct+1;
    };
  };
  else{
   if mc > -1/2 then{
    vv.edge[ff].density:=0;
    vv.edge[ff].color:=CYAN;
    vv.edge[sf].density:=0;
    vv.edge[sf].color:=CYAN;
    id1 := fid(vv.id,vv.edge[ff].vertex[1].id,vv.edge[ff].vertex[2].id);
    id2 := fid(vv.id,vv.edge[sf].vertex[1].id,vv.edge[sf].vertex[2].id);
    mw := minimum(vv.vw, minimum(vertex[id1].vw, vertex[id2].vw));
    v1 :=(vertex[id1].__x+vertex[id2].__x-2*vv.__x)/10;
    nv := new_vertex(vv.x+v1[1],vv.y+v1[2]);
    vertex[nv].vw := mw;
    ne := new_edge(nv,vv.id);edge[ne].color:=BLUE;
    ne := new_edge(nv,id1);edge[ne].color:=BLUE;
    ne := new_edge(nv,id2);edge[ne].color:=BLUE;
    ct := ct+1;
    };
  };
};

set edges density 1;
g 10;

};

do{
  ct := 0;
  sc;
}while ct > 0; set edges color BLACK; dt := 1;