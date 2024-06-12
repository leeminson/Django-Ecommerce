var updateBtn=document.getElementsByClassName('update-cart')
for(i=0;i< updateBtn.length;i++)
{
    updateBtn[i].addEventListener('click',function(){
        var prod_id=this.dataset.product
        var act=this.dataset.action
        var quantity=this.dataset.quantity
        console.log('p_id:',prod_id)
        var url= '/add-to-cart/'
        fetch(url,{
            method:'POST',
            headers:{
                'Content-Type':'application/json',
                'X-CSRFToken': csrftoken
            },
            body:JSON.stringify({'product_id':prod_id,'act':act,'quantity':quantity})
        })
        .then((response)=>{
            return response.json();
        })
        .then((data)=>{
            console.log('data',data)
        })
    })
}