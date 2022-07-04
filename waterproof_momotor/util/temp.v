Require Import Rbase.
Require Import Rfunctions.

Require Import Waterproof.AllTactics.
Require Import Waterproof.notations.notations.
Require Import Waterproof.load_database.RealsAndIntegers.

Open Scope R_scope.

Set Default Goal Selector "!".
Set Default Timeout 5.
Lemma example_reflexivity :
  0 = 0.

Proof.

We conclude that (0 = 0).

Qed.
Lemma exercise_reflexivity :
  3 = 3.
Proof.

Admitted.
Lemma every_x_equal_to_itself :
  for all x : ℝ,
    x = x.

Proof.

Take x : ℝ.

We conclude that (x = x).
Qed.
Lemma exercise :
  for all x : ℝ,
    x + 3 = 3 + x.
Proof.

Help.

Admitted.
Lemma example_choosing : 
  there exists y : ℝ,
    y < 3.

Proof.

Choose y := (2).

We need to show that (y < 3).

We need to show that (2 < 3).

We conclude that (2 < 3).
Qed.
Lemma exercise_choosing :
  there exists z : ℝ,
    10 < z.
Proof.

Admitted.
Lemma example_combine_quantifiers :
  ∀ a : ℝ,
    ∀ b : ℝ,
      ∃ c : ℝ,
        c > b - a.

Proof.

Take a : ℝ.

Take b : ℝ.

Choose c := (b - a + 1).

We need to show that (c > b - a).
We need to show that (b - a + 1 > b - a).
We conclude that (b - a + 1 > b - a).
Qed.
Lemma exercise_combine_quantifiers :
  ∀ x : ℝ,
    ∀ y : ℝ,
      ∃ z : ℝ,
        x < z - y.
        
Proof.

Admitted.

Lemma example_assumptions :
  ∀ a : ℝ, a < 0 ⇒ - a > 0.

Proof.

Take a : ℝ.
We need to show that 
  ((a < 0) ⇒ (-a > 0)).

Assume a_lt_0 : (a < 0).
We need to show that (-a > 0).
We conclude that (-a > 0).
Qed.
Lemma exercise_assumptions :
  ∀ a : ℝ, (∀ b : ℝ, ( a > 0 ⇒ (b > 0 ⇒ a + b > -1))).
  
Proof.

Admitted.

Lemma example_inequalities :
  ∀ ε : ℝ, ε > 0 ⇒ Rmin ε 1 < 2.
Proof.
Take ε : ℝ.
Assume ε_gt_0 : (ε > 0).
We conclude that
  (&  Rmin ε 1 &≤ 1
               &< 2).
Qed.
Lemma exercise_inequalities :
  ∀ ε : ℝ, ε > 0 ⇒ Rmin (ε / 2) 1 < ε.
  
Proof.

Admitted.
Lemma example_backwards :
  ∀ ε : ℝ,
    ε > 0 ⇒
      3 + Rmax ε 2 ≥ 3.
Proof.
Take ε : ℝ.
Assume ε_gt_0 : (ε > 0).

It suffices to show that (Rmax ε 2 ≥ 0).

Rewrite inequality (Rmax ε 2) "≥" (2) "≥" 0.
Qed.
Lemma exercise_backwards :
  ∀ ε : ℝ, ε > 0 ⇒ 5 - Rmax ε 3 ≤ 5.

Admitted.
Lemma example_smaller_steps :
  ∀ ε : ℝ, ε > 0 ⇒
    4 - Rmax ε 1 ≤ 3.
Proof.
Take ε : ℝ.
Assume ε_gt_0 : (ε > 0).


It holds that Rmax_gt_1 : (Rmax ε 1 ≥ 1).

We conclude that (4 - Rmax ε 1 ≤ 3).
Qed.

Lemma exercise_smallers_steps :
  ∀ ε : ℝ, ε > 0 ⇒
    3 + Rmax 2 ε ≥ 5. 
    
Proof.

Admitted.
Lemma example_use_for_all :
  ∀ x : ℝ, ∀ y : ℝ,
    (∀ δ : ℝ, δ > 0 ⇒ x < δ) ⇒
      (∀ ε : ℝ, ε > 0 ⇒ y < ε) ⇒
        x + y < 1.
Proof.
Take x : ℝ. Take y : ℝ.
Assume del_cond : (∀ δ : ℝ, δ > 0 ⇒ x < δ).
Assume eps_cond : (∀ ε : ℝ, ε > 0 ⇒ y < ε).


By del_cond it holds that x_lt_half : (x < 1/2).

By (eps_cond (1/2)) it holds that y_lt_half : (y < 1/2).

We conclude that (x + y < 1).
Qed.
Lemma exercise_use_for_all:
  ∀ x : ℝ,
    (∀ ε : ℝ, ε > 0 ⇒ x < ε) ⇒
      10 * x < 1.
      
Proof.

Admitted.

Lemma example_use_there_exists :
  ∀ x : ℝ,
    (∃ y : ℝ, 10 < y ∧ y < x) ⇒
      10 < x.
Proof.
Take x : ℝ.
Assume exists_y_with_prop : (∃ y : ℝ, 10 < y ∧ y < x).


Choose y such that 
  y_gt_10_and_x_gt_y according to exists_y_with_prop.

We conclude that
  (&  10 &< y
         &< x).
Qed.
Lemma exercise_use_there_exists :
  ∀ z : ℝ,
    (∃ x : ℝ, (x < -5) ∧ (z > x^2)) ⇒
      25 < z.
      
Proof.

Admitted.
Lemma example_contradiction :
  ∀ x : ℝ,
   (∀ ε : ℝ, ε > 0 ⇒ x < ε) ⇒
     x ≤ 0.
Proof. 
Take x : ℝ.
Assume eps_cond : (∀ ε : ℝ, ε > 0 ⇒ x < ε).
We need to show that (x ≤ 0).

We argue by contradiction.

Assume not_x_le_0 : (¬ (x ≤ 0)).
It holds that x_gt_0 : (x > 0).
By eps_cond it holds that x_lt_x_div_2 : (x < x/2).
It holds that x_le_0 : (x ≤ 0).

Contradiction.
Qed.
Lemma exercise_contradiction :
  ∀ x : ℝ,
    (∀ ε : ℝ, ε > 0 ⇒ x > 1 - ε) ⇒
      x ≥ 1.
      
Proof.

Admitted.
Lemma example_cases : 
  ∀ x : ℝ, ∀ y : ℝ,
    Rmax x y = x ∨ Rmax x y = y.
Proof. 
Take x : ℝ. Take y : ℝ.

Either (x < y) or (x ≥ y).
- Case (x < y).
  It suffices to show that (Rmax x y = y).
  By Rmax_right we conclude that (Rmax x y = y).
- Case (x ≥ y).
  It suffices to show that (Rmax x y = x).
  By Rmax_left we conclude that (Rmax x y = x).
Qed.
Lemma exercises_cases :
  ∀ x : ℝ, ∀ y : ℝ,
    Rmin x y = x ∨ Rmin x y = y.
    
Proof.

Admitted.
Lemma example_both_statements:
  ∀ x : ℝ, x^2 ≥ 0 ∧ | x | ≥ 0.
Proof.
Take x : ℝ.

We show both statements.

- We need to show that (x^2 ≥ 0).
  We conclude that (x^2 ≥ 0).
- We need to show that (| x | ≥ 0).
  We conclude that (| x | ≥ 0).
Qed.
Lemma exercise_both_statements:
  ∀ x : ℝ, 0 * x = 0 ∧ x + 1 > x.
  
Proof.

Admitted.
Lemma example_both_directions:
  ∀ x : ℝ, ∀ y : ℝ,
    x < y ⇔ y > x.
Proof.
Take x : ℝ. Take y : ℝ.


We show both directions.

- We need to show that (x < y ⇒ y > x ).
  Assume x_lt_y : (x < y).
  We conclude that (y > x).
- We need to show that (y > x ⇒ x < y ).
  Assume y_gt_x : (y > x).
  We need to show that (x < y).
  We conclude that (x < y).
Qed.
Lemma exercise_both_directions:
  ∀ x : ℝ, x > 1 ⇔ x - 1 > 0.
  
Proof.

Admitted.
Lemma example_induction :
  ∀ n : ℕ → ℕ, (∀ k : ℕ, (n k < n (k + 1))%nat) ⇒
    ∀ k : ℕ, (k ≤ n k)%nat.
Proof.
Take n : (ℕ → ℕ).
Assume n_increasing : (∀ k : ℕ, (n k < n (k + 1))%nat).

We use induction on k.
- We first show the base case, namely ( (0 ≤ n 0)%nat ).
  We conclude that (0 ≤ n 0)%nat.
- We now show the induction step.
  Assume IH : (k ≤ n k)%nat.
  It holds that n_k_lt_n_k_plus_1 : (n k < n (k + 1))%nat.
  We conclude that (k + 1 ≤ n (k + 1))%nat.
Qed.
Lemma exercise_induction :
  ∀ f : ℕ → ℕ, (∀ k : ℕ, (f (k + 1) = f k)%nat) ⇒
    ∀ k : ℕ, (f k = f 0)%nat.
    
Proof.

Admitted.

Definition square (x : ℝ) := x^2.
Lemma example_expand :
  ∀ x : ℝ, square x ≥ 0.
Proof.
Take x : ℝ.

Expand the definition of square.

That is, write the goal as (x^2 ≥ 0).
We conclude that (x^2 ≥ 0).
Qed.
Lemma exercise_expand :
  ∀ x : ℝ, - (square x) ≤ 0.
  
Proof.

Admitted.