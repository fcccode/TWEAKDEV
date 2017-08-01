#include <dlfcn.h>


@interface QMLoader:NSObject
@end


@implementation QMLoader

+ (instancetype) sharedInstance
{
	static dispatch_once_t onceToken ; 
	static QMLoader *_sharedInstance ;
	dispatch_once (&onceToken , ^{
		_sharedInstance = [[self alloc] init] ; 
	});

	return  _sharedInstance
} 


- (void) show
{
	Class FLEXManager =NSClassFromString(@"FLEXManager") ; 
	id sharedManager = [FLEXManager performSelector:@selector(sharedManager)]; 
	[sharedManager performSelector:@selector(showExplorer)] ;
}

@end


%ctor{

	NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init] ; 
	NSDictionary *prefs = [NSDictionary dictionaryWithContentOfFile:@"/var/mobile/Library/Preferences/com.niko.qm.plist"] ;
	NSString *libraryPath = @"/Library/Application Support/FLEXLoader/FLEX.framework/FLEX";

	NSString *keyPath = [NSString stringWithFormat:@"FLEXLoaderEnabled-%@", [[NSBundle mainBundle]bundleIdentifier]] ;
	NSLog(@"%@ %@" , libraryPath , prefs) ; 
	if([[prefs objectForKey:keyPath] boolValue]){
		if([[NSFileManager defaultManager] fileExistsAtPath:libraryPath])
		{
			void *handle = dlopen([libraryPath UTF8String],)
			if(handle == NULL)
			{
				NSLog(@"open lib error");
			}
			else
			{
				NSLog(@"open lib ok");
				[[NSNotificationCenter defaultCenter] 
						addObserver:[QMLoader sharedInstance] 
						selector:@selector(show)
						name:UIApplicationDidBecomeActiveNotification
						object:nil	];
			}
		}

	}
	else
	{
		NSLog("ggggggggggg");
	}
	NSLog("loaded");
	[pool drain];

} 