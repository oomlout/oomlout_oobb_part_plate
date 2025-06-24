$fn = 50;


difference() {
	union() {
		hull() {
			translate(v = [-152.0000000000, 2.0000000000, 0]) {
				cylinder(h = 9, r = 5);
			}
			translate(v = [152.0000000000, 2.0000000000, 0]) {
				cylinder(h = 9, r = 5);
			}
			translate(v = [-152.0000000000, -2.0000000000, 0]) {
				cylinder(h = 9, r = 5);
			}
			translate(v = [152.0000000000, -2.0000000000, 0]) {
				cylinder(h = 9, r = 5);
			}
		}
	}
	union() {
		translate(v = [-150.0000000000, 0.0000000000, 0]) {
			cylinder(h = 9, r = 3.2500000000);
		}
		translate(v = [-150.0000000000, 0.0000000000, 0]) {
			cylinder(h = 9, r = 1.8000000000);
		}
		translate(v = [-150.0000000000, 0.0000000000, 0]) {
			cylinder(h = 9, r = 1.8000000000);
		}
		translate(v = [-150.0000000000, 0.0000000000, 0]) {
			cylinder(h = 9, r = 1.8000000000);
		}
	}
}