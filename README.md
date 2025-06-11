# Prime-cycle-method
Anonymous method to filter prime numbers using cyclic digit pattern
### how it works
it stars with a repeating digit pattern:
7,1,3,7,9,3,9,1
2. Numbers ending with this pattern are considered **prime candidates**.
3. False positives (like 7×7=49, 11×7=77) are eliminated by removing all numbers that are products of other candidates.
4. The result is a refined list of probable prime numbers.

### ⚙️ Code

Check the `prime_cycle.py` file to run the logic.

### 🔓 License

Released under the GPL v3 License.  

