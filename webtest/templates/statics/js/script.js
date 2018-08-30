$(document).ready(function(){
    $("#login").click(function(){
        var user = $("#username").val();
        var pwd = $("#password").val();
        var pd={"username":user,"password":pwd};
        $.ajax({
            type:"post",
            url:"/",
            data:pd,
            cache:false,
            success:function(data){
                if(data=="your password was not right.")
                    {
                        alert(data);
                    }
                else if(data=="There is no this user.")
                    {
                        alert(data);
                    }
                else
                    {
                        window.location.href="/user?user="+data;
                    }
            },
            error:function(){
                alert("error!");
            },
        });
    });
});
