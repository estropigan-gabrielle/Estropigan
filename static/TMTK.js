			function showCompare(price){
			    console.log('Show Modal');
			    document.querySelector('#modal-compare').style.display = 'flex';
			    document.querySelector('#price').value = price;
			}

			function showModal(){
			}

				function hideModal(){
				    console.log('Hide Modal');
				    document.querySelector('#modal-compare').style.display = 'none';
			}

			function comparePrice(){
			    let price = document.querySelector('#price').value;
			    let cash = document.querySelector('#cash').value;
			    console.log(price);
			    console.log(cash);
			    console.log(Number(cash) >= Number(price));
			    console.log(Number(price) - Number(cash));

			    if (Number(cash) == Number(price)){
			    	document.querySelector('#message-equal').style.display = 'flex';
			    	document.querySelector('#message-enough').style.display = 'none';
			        document.querySelector('#message-short').style.display = 'none';
			        document.querySelector('#equal').innerHTML = 'Your budget is enough!';
			    }
			    else if(Number(cash) >= Number(price)){
			        document.querySelector('#message-enough').style.display = 'flex';
			        document.querySelector('#message-short').style.display = 'none';
			        document.querySelector('#message-equal').style.display = 'none';
			        document.querySelector('#enough').innerHTML = 'You have enough budget! \nYou have an extra ₱' + [(Number(cash)).toString()-Number(price)]+'\nCheck and review more items!';
			    }

			    else{
			        document.querySelector('#message-short').style.display = 'flex';
			        document.querySelector('#message-enough').style.display = 'none';
			        document.querySelector('#message-equal').style.display = 'none';
			        document.querySelector('#short').innerHTML = 'You don\'t have enough budget! \nYou need additional ₱' +  (Number(price) - Number(cash)).toString();
			    }
			}	