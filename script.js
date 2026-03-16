const symbols = ["🍒","🍋","🍊","🍉","🍇","7️⃣"];

function spin(){
  const s1 = symbols[Math.floor(Math.random()*symbols.length)];
  const s2 = symbols[Math.floor(Math.random()*symbols.length)];
  const s3 = symbols[Math.floor(Math.random()*symbols.length)];
  
  document.getElementById("slot1").innerText = s1;
  document.getElementById("slot2").innerText = s2;
  document.getElementById("slot3").innerText = s3;
  
  if(s1===s2 && s2===s3){
    document.getElementById("result").innerText = "🎉 You Won! +10 Coins";
  } else {
    document.getElementById("result").innerText = "Try Again!";
  }
}
