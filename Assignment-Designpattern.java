
import java.util.*;
public class colorgame {

  
  public static void main(String[] args) {
    
   Scanner sc=new Scanner(System.in);
   apple apple=new apple();
   banana banana=new banana();
   frog frog=new frog();
   
   HashMap<String,Object> objects=new HashMap<String,Object>();
   objects.put("apple", apple);
   objects.put("banana", banana);
   objects.put("frog", frog);
   Command subscribe = new SubscribeCommand();
   Command unsubscribe = new UnsubscribeCommand();
   while(true){
	   String cmd=sc.nextLine();
	   if(cmd.equals("exit"))
		   return;
	   
	   if(cmd.charAt(0)=='+'){
		   String substr=cmd.substring(1);
		   subscribe.execute((subscribeunsubscribe) objects.get(substr));
		   
	   }
	   else if(cmd.charAt(0)=='-'){
		   String substr=cmd.substring(1);
		   unsubscribe.execute((subscribeunsubscribe) objects.get(substr));
	   }
	   else{
		   Notify not = new NotifyCommand();
		   for(Object t:objects.values()){
			   not.executenot((subscribeunsubscribe) t, cmd);
		   }
	   }
   }
   
	   
   }
  
  public static Object createObject(String obj){
	  Object object = null;
	  switch(obj){
	  case "apple": object=new apple();
	  }
	  return object;
  	}
  
  

  
  public static interface subscribeunsubscribe {
    public void subscribe();
    public void unsubscribe();
    public void notifyObject(String color);
  }

  public static class apple implements subscribeunsubscribe {
	private boolean subscribe=false;
	private String obj="apple";
	private String[] colors={"red","green"};
    public void subscribe() {
      this.subscribe=true;
      System.out.println("Subscribing apple");
    }

    public void unsubscribe() {
      if(this.subscribe){
    	this.subscribe=false;
      System.out.println("Unsubcribing apple");
      }
    }
    
    public boolean getStatus(){
    	return this.subscribe;
    }
    
    public void notifyObject(String color){


    	if(this.subscribe){
    		for(String c:this.colors){
    			if(c.equals(color))
    		System.out.println("Hey I am apple, I am "+color+" Sometimes");
    		}
    	}
    }
  }
  public static class banana implements subscribeunsubscribe {
		private boolean subscribe=false;
		private String[] colors={"yellow"};
	    public void subscribe() {
	      this.subscribe=true;
	      System.out.println("Subscribing banana");
	    }

	    public void unsubscribe() {
	      if(this.subscribe){
	    	this.subscribe=false;
	      System.out.println("Unsubcribing banana");
	      }
	    }
	    
	    public boolean getStatus(){
	    	return this.subscribe;
	    }
	    
	    public void notifyObject(String color){

	    	if(this.subscribe){
	    		for(String c:this.colors){
	    			if(c.equals(color))
	    		System.out.println("Hey I am banana, I am "+color+" Sometimes");
	    		}
	    	}
	  }
  }
  public static class frog implements subscribeunsubscribe {
		private boolean subscribe=false;
		private String[] colors={"blue","green"};
	    public void subscribe() {
	      this.subscribe=true;
	      System.out.println("Subscribing frog");
	    }

	    public void unsubscribe() {
	      if(this.subscribe){
	    	this.subscribe=false;
	      System.out.println("Unsubcribing frog");
	      }
	    }
	    
	    public boolean getStatus(){
	    	return this.subscribe;
	    }
	    
	    public void notifyObject(String color){
	    	
	    	if(this.subscribe){
	    		for(String c:this.colors){
	    			if(c.equals(color))
	    		System.out.println("Hey I am frog, I am "+color+" Sometimes");
	    		}
	    	}
	    }
	  }
  public interface Command {
    public void execute(subscribeunsubscribe a);
    
  }
  public interface Notify{
	  public void executenot(subscribeunsubscribe device,String color);
  }
  public static class SubscribeCommand implements Command {

    public void execute(subscribeunsubscribe device) {
       device.subscribe();
    }
  }

  public static class UnsubscribeCommand implements Command {

    public void execute(subscribeunsubscribe device) {
       device.unsubscribe();
    }
  }
  public static class NotifyCommand implements Notify {

	    public void executenot(subscribeunsubscribe device,String color) {
	      device.notifyObject(color);
	    }
	  }
}