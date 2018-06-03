import java.rmi.*;

public interface RMIInterface extends Remote
{
	public String Hello()throws RemoteException;

	public void getOffsetOfMachine1(int client_1_offset)throws RemoteException;
	public void getOffsetOfMachine2(int client_2_offset)throws RemoteException;
	public int getServerLocalTime()throws RemoteException;
	public void calculateNetOffset(int client_1_offset_server, int client_2_offset_server)throws RemoteException;
	/*public String Multiplication(int a,int b)throws RemoteException;
	public String Division(int a,int b)throws RemoteException;*/
}