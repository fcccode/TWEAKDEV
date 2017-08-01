#import <substrate.h>
#import <mach-o/dyld.h>
#import <dlfcn.h>

int fake_ptrace(int request , pid_t pid , caddr_t addr , int data){
	return 0 ; 
}



void *(*old_dlsym)(void *handle , const char *symbol) ; 


void *my_dlsym(void *handle , const char *symbol)
{
	if(!strcmp(symbol , "ptrace"))
	{

		return (void *)fake_ptrace ; 
	}

	return  old_dlsym(handle , symbol) ; 
}



%ctor{
	[[[UIAlertView  alloc] initWithTitle:@"nikos233" message:@"message" delegate:nil cancelButtonTitle:@"ok"  otherButtonTitles:nil] show];
	MSHookFunction((void *)dlsym , (void *)my_dlsym , (void **)&old_dlsym) ; 
}
