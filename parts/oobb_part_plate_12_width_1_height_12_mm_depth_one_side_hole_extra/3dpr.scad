$fn = 50;


difference() {
	union() {
		hull() {
			translate(v = [-84.5000000000, 2.0000000000, 0]) {
				cylinder(h = 12, r = 5);
			}
			translate(v = [84.5000000000, 2.0000000000, 0]) {
				cylinder(h = 12, r = 5);
			}
			translate(v = [-84.5000000000, -2.0000000000, 0]) {
				cylinder(h = 12, r = 5);
			}
			translate(v = [84.5000000000, -2.0000000000, 0]) {
				cylinder(h = 12, r = 5);
			}
		}
	}
	union() {
		translate(v = [-82.5000000000, 0.0000000000, 0]) {
			cylinder(h = 12, r = 3.2500000000);
		}
		translate(v = [-82.5000000000, 0.0000000000, 0]) {
			cylinder(h = 12, r = 1.8000000000);
		}
		translate(v = [-82.5000000000, 0.0000000000, 0]) {
			cylinder(h = 12, r = 1.8000000000);
		}
		translate(v = [-82.5000000000, 0.0000000000, 0]) {
			cylinder(h = 12, r = 1.8000000000);
		}
	}
}