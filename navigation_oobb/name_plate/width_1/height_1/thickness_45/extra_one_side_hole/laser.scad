$fn = 50;


difference() {
	union() {
		cylinder(h = 45, r = 7.0000000000);
	}
	union() {
		cylinder(h = 45, r = 3.0000000000);
		cylinder(h = 45, r = 1.5000000000);
		cylinder(h = 45, r = 1.5000000000);
		cylinder(h = 45, r = 1.5000000000);
	}
}