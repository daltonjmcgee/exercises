function checkCashRegister(price, cash, cid) {
  var totalCid = 0,
      change = (cash-price),
      toChange = change,
      availCash = {},
      refundCash = {},
      refund = []
  for (let x in cid){
    totalCid+=cid[x][1];
    availCash[cid[x][0]] = cid[x][1];
    refundCash[cid[x][0]] = 0;

  }
  totalCid = Number(totalCid.toFixed(2))
  function getChange(){
    if(totalCid<change)return "Insufficient Funds";
    if(totalCid===change)return "Closed";
    if (toChange>=100 && availCash["ONE HUNDRED"]>=100){
      toChange-=100;
      availCash["ONE HUNDRED"]-=100;
      refundCash["ONE HUNDRED"]+=100;
      getChange();
    }
    else if (toChange>=20 && availCash["TWENTY"]>=20){
      toChange-=20;
      availCash["TWENTY"]-=20;
      refundCash["TWENTY"]+=20;
      getChange();
    }
    else if (toChange>=10 && availCash["TEN"]>=10){
      toChange-=10;
      availCash["TEN"]-=10;
      refundCash["TEN"]+=10;
      getChange();
    }
    else if (toChange>=5 && availCash["FIVE"]>=5){
      toChange-=5;
      availCash["FIVE"]-=5;
      refundCash["FIVE"]+=5;
      getChange();
    }
    else if (toChange>=1 && availCash["ONE"]>=1){
      toChange-=1;
      availCash["ONE"]-=1;
      refundCash["ONE"]+=1;
      getChange();
    }
    else if (toChange>=0.25 && availCash["QUARTER"]>=0.25){
      toChange-=0.25;
      availCash["QUARTER"]-=0.25;
      refundCash["QUARTER"]+=0.25;
      getChange();
    }
    else if (toChange>=0.10 && availCash["DIME"]>=0.10){
      toChange-=0.10;
      availCash["DIME"]-=0.10;
      refundCash["DIME"]+=0.10;
      getChange();
    }
    else if (toChange>=0.05 && availCash["NICKEL"]>=0.05){
      toChange-=0.05;
      availCash["NICKEL"]-=0.05;
      refundCash["NICKEL"]+=0.05;
      getChange();
    }
    else if (toChange>=0.01 && availCash["PENNY"]>=0.01){
      toChange-=0.01;
      availCash["PENNY"]-=0.01;
      refundCash["PENNY"]+=0.01;
      toChange = Number(toChange.toFixed(2))
      getChange();
    }
    if (toChange>0){return "Insufficient Funds"}

    return Object.entries(refundCash).reverse().filter(x=>x[1]>0)
  }
  return getChange()
}


checkCashRegister(3.26, 100.00, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.10], ["QUARTER", 4.25], ["ONE", 90.00], ["FIVE", 55.00], ["TEN", 20.00], ["TWENTY", 60.00], ["ONE HUNDRED", 100.00]]);
