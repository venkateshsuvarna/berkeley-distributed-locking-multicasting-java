import java.rmi.*;
import java.rmi.server.*;
import java.rmi.registry.*;

import java.util.*;
public class RMIServer extends UnicastRemoteObject implements RMIInterface
{
	String key="Mpstme";
	int server_local_time;
	int client_1_offset_server;
	int client_2_offset_server;
	
	int client_1_offset_server_recieved=0;
	int client_2_offset_server_recieved=0;
	
	public RMIServer()throws RemoteException
	{
		try
		{
			LocateRegistry.createRegistry(1099);
			Naming.rebind(key,this);
		}
		catch(Exception e)
		{
		 	System.out.println(e);
		}
		
		System.out.println("Enter the Server Initial Logical Clock Time :");
		Scanner sc = new Scanner(System.in);
		int temp;
		temp = sc.nextInt();
		server_local_time=temp;
	}
	public String Hello()throws RemoteException
	{
		return "Hello RMI";
	}
	
	public void getOffsetOfMachine1(int client_1_offset)throws RemoteException
	{
		client_1_offset_server = client_1_offset;
		System.out.println("Offset received from Client 1 :"+client_1_offset_server);
		client_1_offset_server_recieved=1;
		
		if(client_1_offset_server_recieved == 1 && client_2_offset_server_recieved == 1)
		{
			calculateNetOffset(client_1_offset_server, client_2_offset_server);
		}
		
	}
	public void getOffsetOfMachine2(int client_2_offset)throws RemoteException
	{
		client_2_offset_server = client_2_offset;
		System.out.println("Offset received from Client 2 :"+client_2_offset_server);
		client_2_offset_server_recieved=1;
		
		if(client_1_offset_server_recieved == 1 && client_2_offset_server_recieved == 1)
		{
			calculateNetOffset(client_1_offset_server, client_2_offset_server);
		}
	}
	
	public int getServerLocalTime()throws RemoteException
	{
		return server_local_time;
	}
	
	public void calculateNetOffset(int client_1_offset_server, int client_2_offset_server)throws RemoteException
	{
		int temp;
		temp = (client_1_offset_server + client_2_offset_server + 0)/3;
		System.out.println("Net offset is : "+temp);
		server_local_time = server_local_time + temp;
		
	}
	
	/*public String Addition(int a,int b)throws RemoteException
	{	
		int add;
		add=a+b;
		String str_a = Integer.toString(add);
		return str_a;
	}
	public String Subtraction(int a,int b)throws RemoteException
	{

		int sub;
		sub=a-b;
		String str_b = Integer.toString(sub);
		return str_b;
	}
	public String Multiplication(int a,int b)throws RemoteException
	{

		int mul;
		mul=a*b;
		String str_c = Integer.toString(mul);
		return str_c;
	}
	public String Division(int a,int b)throws RemoteException
	{

		int div;
		div=a/b;
		String str_d = Integer.toString(div);
		return str_d;
	}*/

	public static void main(String[] args)
	{
		try
		{
			
			
			new RMIServer();
		}
		catch(Exception e)
		{
			System.out.println(e);
		}
	}
}