import java.rmi.*;
import java.util.Scanner;
public class RMIClient1
{
	String key="rmi://localhost:1099/Mpstme";
	public RMIClient1()
	{
		//int num1;
		//int num2;
		
		int client_1_local_time;
		int server_local_time;
		System.out.println("Enter the Client 1 Initial Logical Clock Time : \n");
		Scanner sc = new Scanner(System.in);
		client_1_local_time = sc.nextInt();
		int client_1_offset;
		
					
			try
			{
				RMIInterface ri=(RMIInterface)Naming.lookup(key);
				System.out.println(ri.Hello());
				
				server_local_time = ri.getServerLocalTime();
				System.out.println("Server Local Time recieved by Client 1 is :"+server_local_time);
				client_1_offset = client_1_local_time - server_local_time;
				System.out.println("Client 1 Offset is : "+client_1_offset);
				ri.getOffsetOfMachine1(client_1_offset);
				
				while(true)
				{
					if(server_local_time != ri.getServerLocalTime())
					{
						client_1_local_time = ri.getServerLocalTime();
						server_local_time = ri.getServerLocalTime();
						System.out.println("Client 1 Local Time got adjusted to : "+client_1_local_time);
						break;
					}
				}
			
				/*Scanner sc=new Scanner(System.in);
				System.out.println("Enter first number:");
				num1=sc.nextInt();
				System.out.println("Enter second number:");
				num2=sc.nextInt();
				System.out.println("Addition :"+ri.Addition(num1,num2));
				System.out.println("Subtraction :"+ri.Subtraction(num1,num2));
				System.out.println("Multiplication :"+ri.Multiplication(num1,num2));
				System.out.println("Division :"+ri.Division(num1,num2));*/
			}
			catch(Exception e)
			{
				System.out.println("Connection to the Berkeley Time Server failed due to the below exception");
				System.out.println(e);
			}
		
		
	}
	
	public static void main(String[] args)
	{
		new RMIClient1();
	}
}